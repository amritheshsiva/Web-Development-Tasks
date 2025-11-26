-- Create database
CREATE DATABASE bookstore;

-- Select database
USE bookstore;

-- Create table "authors"
CREATE TABLE authors(
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(25),
    email VARCHAR(25) UNIQUE
    );

-- Create table "books"
CREATE TABLE books(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_title VARCHAR(25),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );