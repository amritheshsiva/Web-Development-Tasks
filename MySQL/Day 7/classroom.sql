-- Table creation
CREATE TABLE `school`.`student_courses` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(25) NOT NULL , `course` VARCHAR(25) NOT NULL , `score` INT NOT NULL , `email` VARCHAR(25) NOT NULL , `phone` VARCHAR(12) NOT NULL , `city` VARCHAR(25) NOT NULL , `bonus_points` INT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inserting Values
INSERT INTO student_courses
VALUES
(1,'Asha','Python',85,'asha@mail.com','9876543210','Chennai',5),
(2,'Ravi','Python',90,'ravi@mail.com','9876543211','Chennai',NULL),
(3,'Sneha','Java',78,'sneha@mail.com','9876543212','Mumbai',NULL),
(4,'Karan','Java',88,'karan@mail.com','9876543213','Delhi',2),
(5,'Divya','Python',95,'divya@mail.com','9876543214','Mumbai',4),
(6,'Manoj','JavaScript',72,'manoj@mail.com','9876543215','Delhi',NULL);

-- To show the total number of students in each course.
SELECT course,COUNT(name) AS "Total Students"
FROM student_courses
GROUP BY course;

-- To show the average score for each course, but only for courses where the average score is more than 80.
SELECT course,AVG(score)
FROM student_courses
GROUP BY course
HAVING AVG(score)>80;

-- To show names and scores of students who are from Chennai or Mumbai.
SELECT name,score
FROM student_courses
WHERE city="Chennai" OR city= "Mumbai";

-- To show the details of students who don’t have any bonus points.
SELECT * FROM student_courses
WHERE bonus_points IS NULL;

-- To combine the list of student names from Chennai and from Mumbai into a single column list (use UNION).
SELECT name AS "Students from Chennai and Mumbai"
FROM student_courses
WHERE city="Chennai"
UNION
SELECT name
FROM student_courses
WHERE city="Mumbai";
