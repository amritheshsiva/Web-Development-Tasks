-- Database creation
CREATE DATABASE student_registration;
-- Selecting database
USE student_registration;
-- Creating Table "students"
CREATE TABLE students(
student_id INT UNIQUE AUTO_INCREMENT,name VARCHAR(25),email VARCHAR(25) UNIQUE);

-- TO create Table "courses"
CREATE TABLE courses (course_id INT UNIQUE,course_name VARCHAR(25));

-- To create Table "enrollments" linking tables students and courses
CREATE TABLE enrollments(
    student_id INT, 
    course_id INT,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
    );