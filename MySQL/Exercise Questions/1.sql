-- Table creation
CREATE TABLE `school`.`product_items` (`ProductID` INT NOT NULL AUTO_INCREMENT , `ProductCode` INT NOT NULL , `ProductName` VARCHAR(10) NOT NULL , `Price` INT NOT NULL , PRIMARY KEY (`ProductID`)) ENGINE = InnoDB;

-- Inserting into Table
INSERT INTO product_items
VALUES
(1,343,"Food",160),
(2,675,"Soap",35),
(3,874,"Dress",1100),
(4,986,"Phone",12999),
(5,676,"Soap",40),
(6,724,"TV",15999),
(7,254,"Laptop",21060),
(8,725,"TV",1999),
(9,111,"Chair",528),
(10,344,"Food",200),
(11,152,"Plates",160),
(12,178,"Torch",160);

-- To select distinct ProductName from Products table where Price is between 40 and 600.
SELECT DISTINCT ProductName FROM product_items
WHERE Price BETWEEN 40 AND 600;