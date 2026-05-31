-- I AM A COMMENT 

/* 
   This is a multi-line comment
   Used for long explanations
*/

# This is also a comment but single line

SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS STUDENT_ATTENDANCE;

USE STUDENT_ATTENDANCE;

create table STUDENTS(
RollNumber INT PRIMARY KEY,
SName VARCHAR(20),
SDateOfBirth DATE,
GUID CHAR(12)
);

CREATE TABLE GUARDIAN(
GUID CHAR(12) PRIMARY KEY,
GName VARCHAR(20),
GPhone CHAR(10),
GAddress VARCHAR(30)
);

CREATE TABLE ATTENDANCE(
AttendanceDate DATE,
RollNumber INT,
AttendanceStatus CHAR(1),
PRIMARY KEY(AttendanceDate, AttendanceStatus)

);

-- Linking tables using FOREIGN KEY constraints
-- STUDENTS.GUID is linked with GUARDIAN.GUID
-- This means every student record can be connected to a guardian record.

ALTER TABLE STUDENTS
ADD CONSTRAINT fk_students_guardian
FOREIGN KEY (GUID)
REFERENCES GUARDIAN(GUID);

-- ATTENDANCE.RollNumber is linked with STUDENTS.RollNumber
-- This means every attendance record belongs to a valid student.

ALTER TABLE ATTENDANCE
ADD CONSTRAINT fk_attendance_students
FOREIGN KEY (RollNumber)
REFERENCES STUDENTS(RollNumber);

SHOW TABLES;

DESCRIBE GUARDIAN;


