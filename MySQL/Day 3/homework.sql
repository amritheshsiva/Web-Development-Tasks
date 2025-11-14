-- Creating table
CREATE TABLE `school`.`bookstore` (`id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(20) NOT NULL , `author` VARCHAR(20) NOT NULL , `price` INT NOT NULL , `stock_status` VARCHAR(20) NOT NULL , `genre` VARCHAR(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inserting into
Insert INTO bookstore
VALUES(1,"Sky Tales","R. Mehta",350,"In Stock","Fiction"),
(2,"Code Basics","A. Kumar",480,"Out of Stock","Technology"),
(3,"Lost Stars","S. Rao",720,"In Stock","Romance"),
(4,"Math World","P.Singh",280,"In Stock","Education"),
(5,"Craft Ideas","L. Nair",820,"Out of Stock","Hobby");

-- To show all the different genres available in the store (no duplicates).
SELECT DISTINCT genre FROM bookstore;

-- To list all books that are in stock and priced below 400.
SELECT title FROM bookstore
WHERE stock_status="In Stock" AND price<400;

-- To list all books that are either out of stock or have a price above 700.
SELECT title FROM bookstore
WHERE stock_status="Out of Stock" OR price>700;

-- To show the title and price of every book along with a new column that adds 10% GST to the price.
SELECT title,price, price+(price*0.1) AS price_with_gst FROM bookstore;

-- To display the title, price, and stock_status of all books, sorted by price from highest to lowest.
SELECT title,price,stock_status FROM bookstore
ORDER BY price DESC;
