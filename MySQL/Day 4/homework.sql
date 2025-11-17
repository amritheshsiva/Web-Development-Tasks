-- Table creation
CREATE TABLE `school`.`student_database` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(20) NOT NULL , `course` VARCHAR(20) NOT NULL , `fees_paid` INT NOT NULL , `status` VARCHAR(10) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inseritng value
INSERT INTO student_database
VALUES
(1,'Alice','Web Development',5000,'Inactive'),
(2,'Bob','Data Science',7000,'Inactive'),
(3,'Charlie','UI/UX Design',4000,'Active');

-- Query to view only those students whose fees_paid is greater than 5000
SELECT name 
FROM student_database
WHERE fees_paid>5000;

-- To Update the status to 'Active' for students in the 'Web Development' course.
UPDATE student_database
SET status="Active"
WHERE course="Web Development";

-- To Increase the fees_paid by 1000 for students enrolled in 'Data Science'.
UPDATE student_database
SET fees_paid=fees_paid+1000
WHERE course="Data Science";

-- To Update both status to 'Inactive' and reduce fees_paid by 500 for the student whose id is 3.
UPDATE student_database
SET status="Inactive",fees_paid = fees_paid-500
WHERE id=3;

-- Delete the student whose id is 2.
DELETE FROM student_database
WHERE id=2;

-- Delete all students who are 'Inactive'.
DELETE FROM student_database
WHERE status="Inactive";