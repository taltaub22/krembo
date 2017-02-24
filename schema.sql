DROP TABLE IF EXISTS mentors;
CREATE TABLE mentors (
  id        INTEGER PRIMARY KEY AUTO_INCREMENT,
  firstName TEXT NOT NULL,
  lastName  TEXT NOT NULL,
  school    TEXT NOT NULL,
  class     TEXT NOT NULL,
  address   TEXT NOT NULL,
  phone     TEXT NOT NULL,
  shirtSize TEXT NOT NULL
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id            INTEGER PRIMARY KEY          AUTO_INCREMENT,
  firstName     TEXT       NOT NULL,
  lastName      TEXT       NOT NULL,
  address       TEXT       NOT NULL,
  contactName   TEXT       NOT NULL,
  contactPhone  TEXT       NOT NULL,
  photoApproval BOOLEAN    NOT NULL,
  wheelChair    BOOLEAN    NOT NULL,
  comment       MEDIUMTEXT NULL
);
