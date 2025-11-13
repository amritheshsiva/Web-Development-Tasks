-- Creating Table
CREATE TABLE `school`.`books` (`id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(25) NOT NULL , `author` VARCHAR(25) NOT NULL , `price` INT NOT NULL , `genre` VARCHAR(25) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inserting into Table
INSERT INTO books
VALUES(1,"The Great Gatsby","F. Scott Fitzgerald",350,"Fiction"),
(2,"A Brief History of Time","Stephen Hawking",550,"Science"),
(3,"Sapiens","Yuval Noah Harari",480,"History"),
(4,"The Da Vinci Code","Dan Brown",420,"Fiction"),
(5,"The Alchemist","Paulo Coelho",299,"Fiction");

-- Query to display books that have a price greater than 400.
SELECT title FROM books
WHERE price>400;

-- Query to display books where the genre is either 'History', 'Science', or 'Fiction'.
SELECT title FROM books 
WHERE genre IN ("History","Science","Fiction");

-- Query to display book where the title is exactly 'The Great Gatsby'.
SELECT title FROM books 
WHERE title='The Great Gatsby';

-- Query to display all books that are not written by 'Dan Brown'.
SELECT title FROM books 
WHERE author <> "Dan Brown";

