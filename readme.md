---

# 📊 Business Data Mart & Streamlit Application

This project demonstrates to design  **Business Data Mart** using SQL and build a **Streamlit application** to perform **CRUD operations** and generate **business insights**.

---

## 🧩 Project Overview

The application allows the user to:

* Manage customers, products, orders, and order items (CRUD).
* View real-time data from the database.
* Generate sales insights, reports, and visualizations using SQL.
* Identify top customers and top-selling product via Streamlit applicationin Sales Trend Page.


---

## Usage Instructions STREAMLIT APP 

1. After running the application, you can interact with the Streamlit interface to perform CRUD operations.
2. Select the table (Customers, Products, Orders, Order Items) you want to work with.
3. For each table, you can:

   * **Create**: Add new entries via forms.
   * **Read**: View existing entries in a table.
   * **Update**: Modify existing entries.
   * **Delete**: Remove entries.
4.The Sales Trends Page on Streamlit Application can be used to View the Visualisation options these are build using Advanced SQL queries given below and are defined in DataMart.py.


## 🏗️ 1. Setting Up the Project

### ✅ Prerequisites

* Python 3.7+
* MySQL or SQL Workbench (or any RDBMS of your choice)
* pip (Python package manager)

### 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/business-data-mart.git
cd business-data-mart

### 🧪 Create a Virtual Environment for Python

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


## 📁 requirements.txt

Ensure the following packages are in your `requirements.txt`:

```txt

streamlit  
pandas 
mysql.connector
matplotlib.pyplot
streamlit_option_menu 
plotly.express

```

## 📄 File Structure (Example)

```
📦 business-data-mart/
├── app.py
├── requirements.txt
├── README.md
└── database_schema.sql


```
### 📦 Install Python Dependencies

```bash
pip install -r requirements.txt

```

======================================================================================================================


## 🛠️ 2. Database Setup

### 🔧 Create the Database

In MySQL , run the following:

```sql
CREATE DATABASE business_data_mart;

```
### 🗂️ Database Tables
The database consists of four main tables: **Customers**, **Products**, **Orders**, and **Order\_Items**. The schema is defined as follows:
Connect to your database and run the following SQL to create the tables:

```sql
-- show tables in database
show tables;

-- Create CUSTOMER table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Create Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    stock_quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order_Items Table
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    subtotal FLOAT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


########################  NOTE ################################################

### THIS DIRECTORY CONTAIN 3 SQL FILES named as SQL_tables.sql, SQL_CRUD.sql, SQL_adv.sql
to setting up the Database and Fetch Advance query.
PLEASE REFER THESE FILES FOR DETAILED SQL DATABASE AND QUERIES .

---------------------------------------------------------------


## 🚀 3. Running the Streamlit Application

## Usage Instructions STREAMLIT APP 

1. After running the application, you can interact with the Streamlit interface to perform CRUD operations.
2. Select the table (Customers, Products, Orders, Order Items) you want to work with.
3. For each table, you can:

   * **Create**: Add new entries via forms.
   * **Read**: View existing entries in a table.
   * **Update**: Modify existing entries.
   * **Delete**: Remove entries.
4.The Sales Trends Page on Streamlit Application can be used to View the Visualisation options these are build using Advanced SQL queries given below and are defined in DataMart.py.

### 📄 Edit Database Connection in `DataMart.py`

Update the database credentials inside your `connect_db()` function in `DataMart.py`:

```# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # Your MySQL host
        user='root',  # Your MySQL user
        password='password',  # Your MySQL password
        database='business_data_mart'  # Your database name

    )
    print("Connection established")
    return connection

```

### ▶️ Launch the App

```bash
streamlit run DataMart.py

```

The app will open in your browser, usually at `http://localhost:8501`.

## Usage Instructions STREAMLIT APP 

1. After running the application, you can interact with the Streamlit interface to perform CRUD operations.
2. Select the table (Customers, Products, Orders, Order Items) you want to work with.
3. For each table, you can:

   * **Create**: Add new entries via forms.
   * **Read**: View existing entries in a table.
   * **Update**: Modify existing entries.
   * **Delete**: Remove entries.
4.The Sales Trends Page on Streamlit Application can be used to View the Visualisation options these are build using Advanced SQL queries given below and are defined in DataMart.py.


==================================================================

## 🧠 4. Example SQL Queries

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

-- Orders Within a Date Range with Orders Count 
SELECT COUNT(order_id) as Order_Count , order_date  FROM orders 
WHERE order_date BETWEEN '2025-01-01' AND '2025-12-31 '
GROUP BY order_date 
ORDER BY Order_Count DESC;


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

```

========================================================


## 📈 5. Enhancements & Visualizations

* The **Sales Trends Page** on Streamlit Application can be used to View the Visualisation options.
* Dynamic bar charts and Pie Charts for sales Trends are build by  using `st.bar_chart()`, streamlit_option_menu ,plotly.express libraries 
* Filter options for product Type and customer spending
* Input validation for all form fields (e.g., no negative stock or price)
* Use of `st.form()` for smoother user input.


## 📬 Contact

For questions or improvements, feel free to open an issue or contact the maintainer.

---


























---





