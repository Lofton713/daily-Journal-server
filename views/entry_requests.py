import sqlite3
import json
from models.entry import Entry
from models.mood import Mood



def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            j.id,
            j.concept,
            j.entry,
            j.date,
            j.mood_id,
            j.tags,
            m.label
            
        FROM  Journal_entries j
        JOIN Moods m
            on m.id = j.mood_id
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'],
                        row['mood_id'], row['tags'])

            # Create a Location instance from the current row
            mood = Mood(row['id'], row['label'])

            entries.append(entry.__dict__)
            entry.mood = mood.__dict__

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            j.id,
            j.concept,
            j.entry,
            j.date,
            j.mood_id,
            j.tags,
            m.label
            
        FROM Journal_entries J
        JOIN Moods m
            on m.id = j.mood_id
        WHERE j.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'], data['date'],
                            data['mood_id'], data['tags'])

        mood = Mood(data['id'], data['label'])

        entry.mood = mood.__dict__


        return json.dumps(entry.__dict__)

def get_entries_by_mood(mood_id):

    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            j.id,
            j.concept,
            j.date,
            j.mood_id
            j.tags
        from Journals_entries j
        WHERE j.mood_id = ?
        """, ( mood_id, ))

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'],
                                row['mood_id'], row['tags'])
            entries.append(entry.__dict__)

    return json.dumps(entries)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal_entries
        WHERE id = ?
        """, (id, ))
        
def get_entries_by_search(search_terms):

    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            j.id,
            j.concept,
            j.date,
            j.mood_id,
            j.tags
        from Journal_entries j
        WHERE j.concept LIKE ?
        """, ( f'%{search_terms[0]}%' , ))

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'],
                                row['mood_id'], row['tags'])
            
            entries.append(entry.__dict__)

    return json.dumps(entries)

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Journal_entries
            ( concept, entry, date, mood_id, tags )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['concept'], new_entry['entry'],
            new_entry['date'], new_entry['mood_id'], new_entry['tags'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)

def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Journal_entries
            SET
                concept = ?,
                entry = ?,
                mood_id = ?
                tags = ?
                
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'],
            new_entry['mood_id'], new_entry['tags'], id ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
