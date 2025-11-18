-- Table creation
CREATE TABLE `school`.`mobiles` (`id` INT NOT NULL AUTO_INCREMENT , `brand` VARCHAR(20) NOT NULL , `model` VARCHAR(20) NOT NULL , `price` INT NOT NULL , `stock` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- Inserting Value
INSERT INTO mobiles
VALUES
(1,'Samsung','Galaxy M14',12000,30),
(2,'Redmi','Note 12',15000,25),
(3,'Realme','Narzo 50',13000,20),
(4,'Samsung','Galaxy A23',18000,10);

-- To display all mobiles that cost more than 13000 or have stock less than 15.
SELECT brand,model 
FROM mobiles
WHERE price>13000 OR stock<15;

-- To increase the stock by 5 and update the price to 12500 for the mobile with model = 'Narzo 50'.
UPDATE mobiles
SET stock=stock+5, price=12500
WHERE model="Narzo 50";

-- To delete the mobile whose id is 2.
DELETE FROM mobiles
WHERE id=2;

-- Find the lowest and highest price in the table.
SELECT MIN(price)As LowestPrice, MAX(price) AS Largestprice
FROM mobiles;

-- To find the total stock of all mobiles in the table.
SELECT SUM(stock)
FROM mobiles;

-- TO Show the top 2 most expensive mobiles.
SELECT brand,model,price
FROM mobiles
ORDER By price DESC
LIMIT 2;
