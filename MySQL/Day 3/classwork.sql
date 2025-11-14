-- Creating Table
CREATE TABLE `school`.`products` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(15) NOT NULL , `category` VARCHAR(15) NOT NULL , `price` INT NOT NULL , `instock` VARCHAR(15) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inserting into Table
INSERT INTO products  
VALUES 
(1, 'Mouse', 'Electronics', 450, 'No'),
(2, 'USB Cable', 'Electronics', 250, 'Yes'),
(3, 'Lamp','Furniture', 950, 'No'),
(4, 'Notebook', 'Stationery', 45, 'Yes'),
(5, 'Backpack', 'Accessories', 1100, 'No');

-- To show all the unique product categories available in the table.
SELECT DISTINCT category FROM products;

-- To select all products that are in stock and have a price less than 500.
SELECT name FROM products WHERE instock="Yes" AND price<500;

-- To select all products that are not in stock or have a price greater than 1000.
SELECT name FROM products
WHERE instock="No" OR price>1000;

-- To show the names and prices of all products, and sort the results by price from highest to lowest.
Select name,price FROM products
ORDER BY price DESC;

-- TO display the name and an expression showing the price with 18% tax added (label it as price_with_tax).
SELECT name, price+(price*0.18) As price_with_tax
FROM products;
