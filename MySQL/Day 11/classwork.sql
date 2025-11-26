-- Database Creation
CREATE DATABASE lib;

-- Selecting Database
USE lib;

-- Table "authors" creation
CREATE TABLE AUTHORS(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(20)
    );

-- Inserting into table authors
INSERT INTO authors
VALUES(1,'Jane Austen'),
(2,'George Orwell'),
(3,'J.R.R. Tolkien');

-- Table "books" creation
CREATE TABLE books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(20),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
-- To create an index on the author_id column in the books table.
ALTER TABLE books
ADD INDEX (author_id);

-- Inseritng into books table
INSERT INTO books
VALUES
(1,'Pride and Prejudice', 1),
(2,'Sense and Sensibility', 1),
(3,'1984', 2),
(4,'Animal Farm', 2),
(5,'The Hobbit', 3),
(6,'The Fellowship of the Ring', 3);

