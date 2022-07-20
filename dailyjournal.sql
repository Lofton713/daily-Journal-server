DROP TABLE IF EXISTS Journal_Entries;
DROP TABLE IF EXISTS Moods;

CREATE TABLE `Moods`(
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
    ADD CONSTRAINT FOREIGN KEY(`mood_id`) REFERENCES Moods(`id`);
);

CREATE TABLE `Journal_entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept`   TEXT NOT NULL,
    `date`  DATE, 
    `mood_id`   INTEGER NOT NULL
    
);


INSERT INTO `Moods` VALUES ( NULL, "Happy");

INSERT INTO `Moods` VALUES ( NULL, "Sad");
INSERT INTO `Moods` VALUES ( NULL, "Mad");
INSERT INTO `Moods` VALUES ( NULL, "Anxious");
INSERT INTO `Moods` VALUES ( NULL, "Relieved");

INSERT INTO `Journal_entries` VALUES ( NULL, "What is Python?", '2022-07-18', 4);

INSERT INTO `Journal_entries` VALUES ( NULL, "Python is fun", '2022-07-19', 1);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python is hard", '2022-07-20', 2);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python is not too bad", '2022-07-21', 5);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python is impossible!!", '2022-07-22', 3);
INSERT INTO `Journal_entries` VALUES ( NULL, "Python is fun, again! ", '2022-07-18', 1);


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