-- Table creation
CREATE TABLE `school`.`bookstall` (`book_id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(20) NOT NULL , `author` VARCHAR(20) NOT NULL , `price` INT NOT NULL , `stock` INT NOT NULL , PRIMARY KEY (`book_id`)) ENGINE = InnoDB;

-- Value Insertion
INSERT INTO bookstall
VALUES
(1, 'Learn SQL', 'John Smith', 400, 10),
(2, 'Mastering Python', 'Jane Doe', 600, 5),
(3, 'HTML & CSS Basics', 'Alan Webb', 300, 8);

-- To Increase the price of the book 'Learn SQL' by 50 and update its stock to 12.
UPDATE bookstall 
SET price=price+50 ,stock=12 
WHERE title="Learn SQL";

-- Decrease the stock by 2 for books where the price is greater than 500.
UPDATE bookstall
SET stock=stock-2
WHERE price>500;

--TO  Delete the book that has book_id = 3.
DELETE FROM bookstall WHERE book_id=3;



