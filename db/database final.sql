--
-- File generated with SQLiteStudio v3.4.21 on Tue Apr 14 15:37:36 2026
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: User
CREATE TABLE IF NOT EXISTS User
( User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
First_name TEXT NOT NULL,
Last_name TEXT NOT NULL
);
INSERT INTO User (User_ID, First_name, Last_name) VALUES (113, 'Tom', 'HEINZ');
INSERT INTO User (User_ID, First_name, Last_name) VALUES (114, 'Darren', 'JAMES');
INSERT INTO User (User_ID, First_name, Last_name) VALUES (115, 'Jessica', 'Barns');
INSERT INTO User (User_ID, First_name, Last_name) VALUES (116, 'Bob', 'Dylan');

-- Table: Workouts
CREATE TABLE IF NOT EXISTS Workouts
( Workout_ID INTEGER PRIMARY KEY AUTOINCREMENT,
Workout_type TEXT NOT NULL,
Workout duration INTEGER NOT NULL,
Date TEXT NOT NULL,
User_ID INTEGER NOT NULL,
CONSTRAINT  workout_type CHECK (Workout_type IN ("Weight Training","Swimming","Cycling","Incline walking","Fencing"))

CONSTRAINT USER_ID_fk FOREIGN KEY (User_ID)
    REFERENCES User(User_ID));
INSERT INTO Workouts (Workout_ID, Workout_type, Workout, Date, User_ID) VALUES (1224, 'Cycling', 12456, '120579', 114);
INSERT INTO Workouts (Workout_ID, Workout_type, Workout, Date, User_ID) VALUES (11134, 'Swimming', 11245, '120569', 113);
INSERT INTO Workouts (Workout_ID, Workout_type, Workout, Date, User_ID) VALUES (11245, 'Fencing', 12345, '120889', 115);
INSERT INTO Workouts (Workout_ID, Workout_type, Workout, Date, User_ID) VALUES (12456, 'Incline walking', 12345, '120945', 116);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
