-- Table creation
CREATE TABLE `school`.`bookshop` (`id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(30) NOT NULL , `author` VARCHAR(20) NOT NULL , `price` INT NOT NULL , `stock` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inserting values
INSERT INTO bookshop
VALUES
(1,'The Alchemist','Paulo Coelho',350,50),
(2,'Atomic Habits','James Clear',450,40),
(3,'The Psychology of Money','Morgan Housel',400,30),
(4,'Ikigai','Francesc Miralles',300,60),
(5,'Deep Work','Cal Newport',500,20);

-- To display all books that cost less than 450 and have stock more than 30.
SELECT title FROM bookshop
WHERE price<450 AND stock>30;	

-- To update the stock to 45 and reduce the price to 420 for the book titled ‘Deep Work’.
UPDATE bookshop
SET stock=45, price=420
WHERE title='Deep Work';

-- Delete the book titled ‘Ikigai’.
DELETE FROM bookshop
WHERE title='Ikigai';

-- Show the average book price and total number of books currently in the table.
SELECT AVG(price)AS AvgPrice,COUNT(id)AS Total_Books
FROM bookshop;

-- Display the top 3 most expensive books available
SELECT title,price
FROM bookshop
ORDER BY price DESC
LIMIT 3;