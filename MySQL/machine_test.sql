-- Create Database
CREATE DATABASE employee_management;

-- Select Database
USE employee_management;

-- Create Table "Employee"
CREATE TABLE Employee(
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(20),
    Department VARCHAR(20),
    `Leave` INT
    );

--  Inserting values into "Employee" Table
INSERT INTO Employee
VALUES
(1,"Raju","Sales",1),
(2,"Sangeetha","Sales",3),
(3,"Vinay","Operations",8),
(4,"Abey","Packing",2),
(5,"Thomas","Packing",1),
(6,"Muneer","Operations",7),
(7,"Aparna","Sales",3),
(8,"Abid","Operations",9),
(9,"Fathima","Sales",11),
(10,"Varghese","Operations",14);

-- Create Table "Exam"
CREATE TABLE Exam(
    id INT PRIMARY KEY AUTO_INCREMENT,
    Employee_id INT,
    exam_status VARCHAR(10),
    FOREIGN KEY(Employee_id) REFERENCES Employee(id)
    );

--  Inserting values into "Exam" Table
INSERT INTO Exam 
VALUES
(1,2,"Pass"),
(2,5,"Fail"),
(3,1,"Fail"),
(4,8,"Pass"),
(5,3,"Pass"),
(6,1,"Pass"),
(7,6,"Fail"),
(8,9,"Pass"),
(9,10,"Pass");

-- Query to get list of employees who took more than 5 leaves and in sales department.
SELECT Name 
FROM Employee
WHERE `Leave`>5 AND Department = "Sales";

-- Query to get number of employees working in Operations department.
SELECT COUNT(id) AS "No: of Employees in Operations Department"
FROM Employee
WHERE Department="Operations";

-- Single Query to get the count of employees working in each department.
SELECT Department,COUNT(id)AS "No: of Employees"
FROM Employee
GROUP BY Department;

-- Query to list departments where all its employee together took more than 10 leaves.
SELECT Department
FROM Employee
GROUP BY Department
HAVING sum(`Leave`)>10;

-- Query to list employees who passed the exam.
SELECT Name 
FROM Employee
WHERE id IN(
    SELECT Employee_id 
    FROM Exam
    WHERE exam_status="Pass"
    );

-- Query to list employees who have not attended the exam.
SELECT Employee.Name
FROM Employee
LEFT JOIN Exam
ON Exam.Employee_id=Employee.id
WHERE Exam.exam_status IS NULL;