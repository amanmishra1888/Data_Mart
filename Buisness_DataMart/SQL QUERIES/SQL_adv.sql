-- Advanced SQL Queries
-- Total Sales per Product
SELECT Products.product_name, SUM(Order_Items.subtotal) AS total_sales
FROM Order_Items
JOIN Products ON Order_Items.product_id = Products.product_id
GROUP BY Products.product_name
ORDER BY total_sales DESC;

-- Top Customers by Total Spending
SELECT Customers.first_name, Customers.last_name, SUM(Orders.total_amount) AS total_spending
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id
ORDER BY total_spending DESC;

-- Orders Within a Date Range
SELECT * FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-12-31';

-- Create Views for High-Frequency Products
CREATE VIEW High_Frequency_Products AS
SELECT Products.product_name, SUM(Order_Items.quantity) AS total_quantity_sold
FROM Order_Items
JOIN Products ON Order_Items.product_id = Products.product_id
GROUP BY Products.product_name
HAVING total_quantity_sold > 100
ORDER BY total_quantity_sold DESC;

-- Create View for Top Customers
CREATE VIEW Top_Customers2 AS
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING total_spent > 1500;