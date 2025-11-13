-- Creating Table 
CREATE TABLE `school`.`students` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(10) NOT NULL , `age` INT NOT NULL , `department` VARCHAR(25) NOT NULL , `grade` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
-- Inserting into Table
INSERT INTO students 
VALUES 
(1, "Allen", 19, "Computer Science", 85),
(2, "Hemand", 22, "Physics", 92),
(3, "Rahul", 21, "Mechanical", 78),
(4, "Arjun", 23, "Computer Science", 90);


-- Query to display all students whose age is greater than 20.
SELECT name FROM students 
WHERE age>20;

-- Query to display all students in the 'Computer Science' or 'Physics' departments
SELECT name FROM students 
WHERE department IN ("Computer Science","Physics");

-- Query to show the student who has the grade exactly equal to 90.
SELECT name FROM students WHERE grade=90;

-- Query to find students whose grades are between 70 and 90.
SELECT name FROM students WHERE grade BETWEEN 70 AND 90;

