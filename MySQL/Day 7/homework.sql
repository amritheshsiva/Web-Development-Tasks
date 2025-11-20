-- Table creation
CREATE TABLE `school`.`challenges` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(10) NOT NULL , `city` VARCHAR(15) NOT NULL , `score` INT NOT NULL , `bonus` INT NULL DEFAULT NULL , `challenge` VARCHAR(15) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Value inserting
INSERT INTO challenges
VALUES
(1,"Raj","Chennai",88,5,"Fitness"),
(2,"Anu","Mumbai",91,NULL,"Diet"),
(3,"Ravi","Chennai",78,3,"Fitness"),
(4,"Meena","Delhi",82,NULL,"Diet"),
(5,"Farah","Mumbai",95,4,"Fitness"),
(6,"Kiran","Pune",70,NULL,"Yoga"),
(7,"Latha","Pune",87,NULL,"Fitness");

-- To show the details of users whose score is greater than the average score across all users.
SELECT * FROM challenges
WHERE score>(SELECT AVG(score) FROM challenges);

-- TO display the names of users who are participating in the same challenge as the user named 'Farah'.
SELECT name FROM challenges
WHERE challenge=(SELECT challenge FROM challenges WHERE name="Farah");