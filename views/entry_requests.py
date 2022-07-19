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
            j.date,
            j.mood_id,
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
            entry = Entry(row['id'], row['concept'], row['date'],
                          row['mood_id'])

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
            j.date,
            j.mood_id
            
        FROM Journal_entries J
        WHERE j.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'], data['date'],
                            data['mood_id'])

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
        from Journals_entries j
        WHERE j.mood_id = ?
        """, ( mood_id, ))

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['date'],
                                row['mood_id'])
            entries.append(entry.__dict__)

    return json.dumps(entries)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal_entries
        WHERE id = ?
        """, (id, ))
