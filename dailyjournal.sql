DROP TABLE IF EXISTS Journal_Entries;
DROP TABLE IF EXISTS Moods;

CREATE TABLE `Moods`(
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);

CREATE TABLE `Journal_entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept`   TEXT NOT NULL,
    `entry`     TEXT NOT NULL,
    `date`  DATE, 
    `mood_id`   INTEGER NOT NULL,
    `tags` INTEGER 
    
);


INSERT INTO `Moods` VALUES ( NULL, "Happy");

INSERT INTO `Moods` VALUES ( NULL, "Sad");
INSERT INTO `Moods` VALUES ( NULL, "Mad");
INSERT INTO `Moods` VALUES ( NULL, "Anxious");
INSERT INTO `Moods` VALUES ( NULL, "Relieved");

INSERT INTO `Journal_entries` VALUES ( NULL,"Python", "What is Python?", '2022-07-18', 4, 1);

INSERT INTO `Journal_entries` VALUES ( NULL, "Python", "Python is fun", '2022-07-19', 1, 2);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python", "Python is hard", '2022-07-20', 2, 2);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python", "Python is not too bad", '2022-07-21', 5, 2);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python", "Python is impossible!!", '2022-07-22', 3, 3);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python", "Python is fun, again! ", '2022-07-18', 1, 1);


SELECT
    j.id,
    j.concept,
    j.date,
    j.mood_id,
    m.label
FROM  Journal_entries j
JOIN Moods m
    on m.id = j.mood_id

SELECT
    j.id,
    j.concept,
    j.date,
    j.mood_id,
    m.label
            
FROM Journal_entries J
JOIN Moods m
    on m.id = j.mood_id
WHERE j.id = 2

CREATE TABLE `Tags`(
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

DROP TABLE IF EXISTS Entry_tags;

CREATE TABLE `Entry_tags`(
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id` INTEGER,
    `tag_id` INTEGER,
    FOREIGN KEY (`entry_id`) REFERENCES Journal_entries(`id`),
    FOREIGN KEY (`tag_id`) REFERENCES Tags(`id`)
);

INSERT INTO `Tags` VALUES ( NULL, "Action Item");
INSERT INTO `Tags` VALUES ( NULL, "Personal");
INSERT INTO `Tags` VALUES ( NULL, "Work");


SELECT
            t.id,
            t.name
        
        FROM Tags t