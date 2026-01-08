-- I AM A COMMENT 

/* 
   This is a multi-line comment
   Used for long explanations
*/

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

SHOW TABLES;

DESCRIBE GUARDIAN;



