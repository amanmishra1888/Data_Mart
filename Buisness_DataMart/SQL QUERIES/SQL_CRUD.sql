-- CRUD Operations
-- Customers CRUD Operations

-- Create (Add new Customer ):
INSERT INTO Customers (first_name, last_name, email) 
VALUES ('Aman', 'Mishra', 'Aman.Mishra@example.com');

-- Read:Customers Records
SELECT * FROM Customers;

-- Update Customer Table :
UPDATE Customers
SET first_name = 'Jenny', last_name = 'Rocommeta', email = 'jenny.rocometta@example.com',customer_id= 1
WHERE customer_id = 1;

-- Delete Customer :
DELETE FROM Customers WHERE customer_id = 2;

-- PRODUCTS TABLE CRUD
-- Create Product
INSERT INTO Products (product_name, category, price, stock_quantity)
VALUES ('Laptop', 'Electronics', 799.99, 50);
 
 -- Read Products
 SELECT * FROM Products;
 
-- UPDATE Products
UPDATE Products
SET price = 899.99, stock_quantity = 45
WHERE product_id = 1;

-- Delete PRODUCT:
DELETE FROM Products WHERE product_id = 1;

-- Orders CRUD Operations
-- Create New Orders tied to customer:
INSERT INTO Orders (customer_id, total_amount)
VALUES (1, 1599.98);

-- Read Current Orders with Cutomer and Order details:
SELECT * FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id;

-- Update Orders Details for Total Amounts:
UPDATE Orders
SET total_amount = 1899.98
WHERE order_id = 5;

-- Delete Removing Order :
DELETE FROM Orders WHERE order_id = 4;

-- Order_Items CRUD Operations
-- Create:
INSERT INTO Order_Items (order_id, product_id, quantity, subtotal)
VALUES (1, 1, 2, 159.98);

-- Read item in each Order:
SELECT * FROM Order_Items
JOIN Orders ON Order_Items.order_id = Orders.order_id
JOIN Products ON Order_Items.product_id = Products.product_id;

--  Update Existing Qty
UPDATE Order_Items
SET quantity = 3, subtotal = 2399.97
WHERE order_item_id = 1;

-- Delete Remove item form Order
DELETE FROM Order_Items WHERE order_item_id = 1;









