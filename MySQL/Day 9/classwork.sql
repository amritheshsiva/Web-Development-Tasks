-- Create New Database 
CREATE DATABASE library;
--  Select database
USE library;

-- To create table "books"
 CREATE TABLE books(book_id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(20));
--  Inserting into "books" table
INSERT INTO books
VALUES
(1,"The Alchemist"),
(2,"The Power of Now"),
(3,"Think and Grow Rich"),
(4,"Clean Code");

-- To create table "borrowers"
CREATE TABLE borrowers (borrower_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(25),book_id INT);
-- Inserting values into "borrowers"
INSERT INTO borrowers
VALUES
(101,"Alice",1),
(102,"Bob",2),
(103,"Charlie",NULL);

-- To show the list of all books along with the name of the person who borrowed them (if borrowed).
SELECT books.title, borrowers.name
FROM books
LEFT JOIN borrowers
ON books.book_id=borrowers.book_id;

-- To show the list of all borrowers along with the book details they borrowed (if any).
SELECT books.title,borrowers.name
FROM books
INNER JOIN borrowers 
on borrowers.book_id=books.book_id;

-- To show the list of all books that have not been borrowed by anyone.
SELECT books.title
FROM books
LEFT JOIN borrowers
ON books.book_id=borrowers.book_id
WHERE borrowers.name IS NULL;

-- To show the list of all borrowers even if they haven't borrowed any book.

SELECT borrowers.name,books.title
FROM borrowers
LEFT JOIN books
ON books.book_id=borrowers.book_id;