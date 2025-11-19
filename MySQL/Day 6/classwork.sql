-- "books1" table creating
CREATE TABLE `school`.`books1` (`id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(25) NOT NULL , `author` VARCHAR(25) NOT NULL , `genre` VARCHAR(25) NOT NULL , `price` DECIMAL NOT NULL , `copies_sold` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- "bestsellers" Table creating
CREATE TABLE `school`.`bestsellers` (`id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(25) NOT NULL , `author` VARCHAR(25) NOT NULL , `genre` VARCHAR(25) NOT NULL , `price` DECIMAL NOT NULL , `copies_sold` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Table values inside "books1" table
INSERT INTO books1
VALUES
(1,'The Silent Patient','Alex Michaelides','Thriller',399.00,1200),
(2,'Atomic Habits','James Clear','Self-help',499.00,2000),
(3,'The Psychology of Money','Morgan Housel','Finance',350.00,1800);

-- Value inside "bestsellers" table
INSERT INTO bestsellers
VALUES
(4,'Ikigai','Francesc Miralles','Philosophy',300.00,2500),
(5,'Think Like a Monk','Jay Shetty','Self-help',450.00,2200);

-- To show the list of all books from both tables, displaying only the title and author.
SELECT title,author FROM books1
UNION
SELECT title,author FROM bestsellers;

-- To display all books from the books table where the price is greater than 400.
SELECT title FROM books1
WHERE price >400;

-- To show the average price of books in the books table.
SELECT AVG(price)
FROM books1;

-- To display the number of books in the books table using a count.
SELECT COUNT(id) AS 'Total Number of Books'
FROM books1;

-- To show the title and author from books table with aliases Book Title and Written By.
SELECT title AS "Book Title",author AS "Written By"
FROM books1;
