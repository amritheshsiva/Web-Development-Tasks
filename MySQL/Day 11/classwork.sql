-- Database Creation
CREATE DATABASE lib;

-- Selecting Database
USE lib;

-- Table "authors" creation
CREATE TABLE AUTHORS(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(20)
    );
    
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