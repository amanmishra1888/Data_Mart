import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from  streamlit_option_menu import option_menu
import plotly.express as px
from datetime import date


# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # Your MySQL host
        user='root',  # Your MySQL user
        password='password',  # Your MySQL password
        database='test_mart'  # Your database name

    )
    print("Connection established")
    return connection



# CRUD Operations Functions
# --- Customers CRUD ---
#read Customers
def display_customers():
    #Query for Display
    query = "SELECT * FROM Customers"
    # connection establishing and query execution
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    #clossing connection and Writing data
    conn.close()
    st.write(df)

#Add Customers
def add_customer(first_name, last_name, email):

    try:
        #Query for Insert Customer
        query = """
                INSERT INTO Customers (first_name, last_name, email)
                VALUES (%s, %s, %s) 
                """
        #connection establishing and query execution
        conn = get_db_connection()
        cursor = conn.cursor()

        r=cursor.execute(query, (first_name, last_name, email))

        conn.commit()
        conn.close()
    except Exception as e:
        # Handle any other errors
        st.error(f"Unexpected Data Value Input error: {e}")




#Update Customer
def update_customer(customer_id, first_name, last_name, email):
    #Query for Update Customer
    query = """
            UPDATE Customers
            SET first_name = %s, \
                last_name  = %s, \
                email      = %s
            WHERE customer_id = %s \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (first_name, last_name, email, customer_id))
    conn.commit()
    conn.close()

#Delete a CUstomer
def delete_customer(customer_id):
    #Query to Delete Customer
    query = "DELETE FROM Customers WHERE customer_id = %s"
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (customer_id,))
    conn.commit()
    conn.close()


# --- Products CRUD ---

#TO Display a Products
def display_products():
    #Query for Display Products
    query = "SELECT * FROM Products"
    conn = get_db_connection()
    # connection establishing and query execution
    df = pd.read_sql(query, conn)
    conn.close()
    st.write(df)

#Create a Product ENtry
def add_product(product_name, category, price, stock_quantity):
    #Query for Products Adding
    query = """
            INSERT INTO Products (product_name, category, price, stock_quantity)
            VALUES (%s, %s, %s, %s) \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (product_name, category, price, stock_quantity))
    conn.commit()
    conn.close()

#Update Product Table
def update_product(product_id, product_name, category, price, stock_quantity):
    #Query for Update Products
    query = """
            UPDATE Products
            SET product_name   = %s, \
                category       = %s, \
                price          = %s, \
                stock_quantity = %s
            WHERE product_id = %s \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (product_name, category, price, stock_quantity, product_id))
    conn.commit()
    conn.close()

#Delete a Product

def delete_product(product_id):
    #Query to Delete PRoducts
    query = "DELETE FROM Products WHERE product_id = %s"
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(query, (product_id,))
    conn.commit()
    conn.close()


# --- Orders CRUD ---

#Read the Orders
def display_orders():
    #Query to Read
    query = """
            SELECT o.order_id,o.customer_id,  c.first_name, c.last_name, o.order_date, o.total_amount
            FROM Orders o
                     JOIN Customers c ON o.customer_id = c.customer_id \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    st.write(df)

#Create a Order
def add_order(customer_id, total_amount):
    #Query to Insert Order
    query = "INSERT INTO Orders (customer_id, total_amount) VALUES (%s, %s)"
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (customer_id, total_amount))
    conn.commit()
    conn.close()

#update the Order
def update_order(order_id, total_amount):
    #qQuery to Update Order
    query = "UPDATE Orders SET total_amount = %s WHERE order_id = %s"
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (customer_id, total_amount))
    conn.commit()
    conn.close()

#Delete a Order
def delete_order(order_id):
    #Query to Delete ORder
    query = "DELETE FROM Orders WHERE order_id = %s"
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (order_id,))
    conn.commit()
    conn.close()


# --- Order Items CRUD ---
#Display the Order Items
def display_order_items():
    #Query to Display Order Items
    query = """
            SELECT oi.order_item_id, oi.order_id,oi.product_id, p.product_name, oi.quantity, oi.subtotal
            FROM Order_Items oi
                     JOIN Products p ON oi.product_id = p.product_id \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    st.write(df)

# Create a Order Item
def add_order_item(order_id, product_id, quantity, subtotal):
    #Query to Uppate Order Items
    query = """
            INSERT INTO Order_Items (order_id, product_id, quantity, subtotal)
            VALUES (%s, %s, %s, %s) \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (order_id, product_id, quantity, subtotal))
    conn.commit()
    conn.close()

#Udpate a Order Item
def update_order_item(order_item_id, quantity, subtotal):
    #  Query Update for Order Item
    query = """
            UPDATE Order_Items
            SET quantity = %s, \
                subtotal = %s
            WHERE order_item_id = %s \
            """
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (quantity, subtotal, order_item_id))
    conn.commit()
    conn.close()

#Deleete a Order Item
def delete_order_item(order_item_id):
    #Query to  Delete Order Item
    query = "DELETE FROM Order_Items WHERE order_item_id = %s"
    # connection establishing and query execution
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (order_item_id,))
    conn.commit()
    conn.close()


# Function to display sales trend chart
def display_sales_trend():
    #query from Database to get Top Products
    query = "SELECT p.product_name, SUM(oi.subtotal) AS total_sales FROM Order_Items oi JOIN Products p ON oi.product_id = p.product_id GROUP BY p.product_name ORDER BY total_sales DESC"
    # connection establishing and query execution
    conn = get_db_connection()
    sales_data = pd.read_sql(query, conn)
    conn.close()
    #Plotiing Bar Chart using the Data
    plt.figure(figsize=(10, 6))
    #passing the product_name  on X axis and Total sales on y axis
    plt.bar(sales_data['product_name'], sales_data['total_sales'])
    plt.xticks(rotation=90)
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    st.pyplot(plt)

# To Display a Bar Chart for TOP CUSTOMER
def display_top_Customer():
    #Query from Database for TOp Customer
    query = "SELECT Customers.first_name, Customers.last_name, SUM(Orders.total_amount) AS total_spending FROM orders JOIN customers ON orders.customer_id = customers.customer_id GROUP BY customers.customer_id ORDER BY total_spending DESC"
    #Database Connection and Plotiing
    conn = get_db_connection()
    sales_data = pd.read_sql(query, conn)
    conn.close()
    plt.figure(figsize=(10, 6))
    #Taking First_name on X axis and total_Spending on Y axis
    plt.bar(sales_data['first_name'], sales_data['total_spending'])
    plt.xticks(rotation=90)
    plt.title("Top Customer By Spending Category")
    plt.xlabel("first_name")
    plt.ylabel("total_spending")
    #plotting Graph
    st.pyplot(plt)

#To display Pie Chart for Order by Date Range

def display_Orders_Date():
    # Date range input with a default date range
    date_range = st.date_input("Select a date range", [])

    # Make sure the user selected both dates
    if isinstance(date_range, (tuple)) and len(date_range) == 2:
        start_date, end_date = date_range

        st.write("Start date:", start_date, "End date:", end_date)

        query = """
        SELECT COUNT(order_id) AS Order_Count, 
               DATE(order_date) AS order_date  
        FROM orders 
        WHERE order_date BETWEEN %s AND %s 
        GROUP BY order_date 
        ORDER BY Order_Count DESC
        """

        conn = get_db_connection()
        Order_date_wise = pd.read_sql(query, conn, params=[start_date, end_date])
        conn.close()

        if not Order_date_wise.empty:
            # Plot the results
            fig = px.pie(
                Order_date_wise,
                values='Order_Count',
                names='order_date',
                hover_name='order_date',
                title='Order Distribution by Date'
            )
            st.plotly_chart(fig, theme="streamlit")
        else:
            st.warning("No orders found in the selected date range.")
    else:
        st.info("Please select a valid start and end date.")



#Display Horizontal Graph for Customer Spending ON Products
def Customer_Spending_Category():
    # Form for taking entries
    with st.form(key='add_customer_form'):
        options = ["Laptop", "Mobile"]
        selected_options = st.multiselect("Select multiple options:", options)

        st.write(f"You selected: {selected_options}")
        # Assume selected_options is a list of product names
        placeholders = ', '.join(['%s'] * len(selected_options))

        submit_button = st.form_submit_button("Display Trend")
    # IF Button Pressed then Create Customer
    if submit_button:

        #Query to Get Customer Names with Products and Spending
        query = f''' SELECT c.first_name as first_name, o.total_amount AS total_spent,p.product_name as product_name FROM orders o JOIN Customers c ON o.customer_id = c.customer_id  INNER JOIN  orders o1 ON o1.customer_id = c.customer_id  INNER JOIN order_items oi ON o1.order_id=oi.order_id INNER JOIN products p  ON oi.product_id =p.product_id WHERE product_name IN ({placeholders}) '''
        #Database Query and Connection
        conn = get_db_connection()
        Customer_Spending_Category = pd.read_sql(query, conn,params=tuple(selected_options))
        conn.close()
        #Plotiing the Horizontal Bar Chart using  First Name Total Spent and Product Name
        st.bar_chart(Customer_Spending_Category, x='first_name', y='total_spent', color='product_name', horizontal=True)


# Streamlit Interface
st.title("Business Data Mart")

#horizantal Menu
page = option_menu(
    #Giving the MEnu Options as Home, Customer,Orders<Order Items,Sales Trend for Navigation
    menu_title=None,
    options=["Home","Customers", "Products", "Orders", "Order Items", "Sales Trend"],
    icons=["house-dash","people-fill", "headset", "bookmark-check", "card-checklist", "bar-chart-line"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)



# CRUD Operations based on selected page
#Home Page Selected
if page=="Home":
    # Main App

    # Inserts a blank line
    st.markdown("---")
    #Introduction for App
    st.markdown("""
    Welcome to the **Business Datamart Dashboard**! Here you can explore Business Data ,perform Operations on Data, visualize data, and gain insights into your business performance.
    """)
    st.write(" ")
    #insert  an Image
    st.image("buissness.jpg", caption="Business DataMart ")
    st.write(" ")
    st.write(
        """This demo shows how to use Streamlit application to Analyse data for Business.
        Please Navigate to Top Option Menu to explore the Application."""
    )


#Customer Page Selected
elif page == "Customers":
    #TO Read Customers
    st.subheader("Customer List")
    st.write(" ")

    display_customers()
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
#To Create a Customer
    st.subheader("Add New Customer")
    st.write(" ")
    #Form for taking entries
    with st.form(key='add_customer_form'):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        submit_button = st.form_submit_button("Add Customer")
        # IF Button Pressed then Create Customer
        if submit_button:

            add_customer(first_name, last_name, email)
            st.success("Customer added successfully!")
            #Create and Displey Customers
            display_customers()
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #Update Customer
    st.subheader("Update Customer")
    st.write(" ")
    #Form taking Customer Entry
    with st.form(key='update_customer_form'):
        customer_id = st.number_input("Customer ID to Update", min_value=1, step=1)
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        #Button pressed to Update Customer
        submit_button = st.form_submit_button("Update Customer")
        if submit_button:
            update_customer(customer_id, first_name, last_name, email)
            st.success("Customer updated successfully!")
            display_customers()
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #To Delete Customer
    st.subheader("Delete Customer")
    st.write(" ")
    #Customer ids for Delete
    customer_id_to_delete = st.number_input("Customer ID to Delete", min_value=1, step=1)
    if st.button("Delete Customer"):
        #Button Preeed to Delte Customer
        delete_customer(customer_id_to_delete)
        st.success(f"Customer {customer_id_to_delete} deleted successfully!")
        display_customers()
# If Products Selected
elif page == "Products":
    #Read Products
    st.subheader("Product List")
    st.write(" ")
    display_products()
    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #To add Product using Form Entries
    st.subheader("Add New Product")
    st.write(" ")
    with st.form(key='add_product_form'):
        product_name = st.text_input("Product Name")
        category = st.text_input("Category")
        price = st.number_input("Price", min_value=0.0, step=0.01)
        stock_quantity = st.number_input("Stock Quantity", min_value=0, step=1)
        #if Button Pressed then Add Product
        submit_button = st.form_submit_button("Add Product")
        if submit_button:
            add_product(product_name, category, price, stock_quantity)
            st.success("Product added successfully!")
            display_products()

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("---")

    st.write(" ")
    st.write(" ")
    st.write(" ")
    # TO Update Product
    st.subheader("Update Product")
    st.write(" ")
    #get Values from User using Form
    with st.form(key='update_product_form'):
        product_id = st.number_input("Product ID to Update", min_value=1, step=1)
        product_name = st.text_input("Product Name")
        category = st.text_input("Category")
        price = st.number_input("Price", min_value=0.0, step=0.01)
        stock_quantity = st.number_input("Stock Quantity", min_value=0, step=1)
        submit_button = st.form_submit_button("Update Product")
        #If Button pressed then Update Product
        if submit_button:
            update_product(product_id, product_name, category, price, stock_quantity)
            st.success("Product updated successfully!")
            display_products()

    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #Delete a Product
    st.subheader("Delete Product")
    st.write(" ")
    # get Values in Form
    product_id_to_delete = st.number_input("Product ID to Delete", min_value=1, step=1)
    if st.button("Delete Product"):
        #if Button Pressed then Delete Product
        delete_product(product_id_to_delete)
        st.success(f"Product {product_id_to_delete} deleted successfully!")
        display_products()
# if Orders Selected
elif page == "Orders":
    #Display ORders
    st.subheader("Order List")
    st.write(" ")
    display_orders()

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #add ORder using the Values in Form
    st.subheader("Add New Order")
    st.write(" ")
    with st.form(key='add_Order_form'):
        customer_id = st.number_input("Customer Id", min_value=0, step=1)
        total_amount = st.number_input("Total Amount", min_value=0.0, step=0.01)
        submit_button = st.form_submit_button("Add Order")
        #IF button pressed then Add Orders and display
        if submit_button:
            add_order(customer_id, total_amount)
            st.success("Order added successfully!")
            display_orders()

    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("---")

    st.write(" ")
    st.write(" ")
    st.write(" ")


#Update Orders using Form Values
    st.subheader("Update Orders")
    st.write(" ")
    #get input Values in Form
    with st.form(key='update_Order_form'):
        order_id = st.number_input("Order Id", min_value=0, step=1)
        total_amount = st.number_input("Total Amount", min_value=0.0, step=0.01)

        submit_button = st.form_submit_button("Update Order")
        #If Button is preeed then Update Orders
        if submit_button:
            update_order(order_id, total_amount)
            st.success("Order updated successfully!")
            display_orders()
    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
#To Delete Orders
    st.subheader("Delete Order")
    st.write(" ")
    #get Order id to delete
    order_id_to_delete = st.number_input("Order ID to Delete", min_value=1, step=1)
    #if Button Pressed then Delete Orders
    if st.button("Delete Order"):
        delete_order(order_id_to_delete)
        st.success(f"Order {order_id_to_delete} deleted successfully!")
        #display Orders after Delete to check
        display_orders()


#if Order Item is Selected

elif page == "Order Items":
    st.write(" ")
    #TO display Order List
    st.subheader("Order Items List")
    display_order_items()

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #To Add New Orders Form
    st.subheader("Add New Order Items")
    st.write(" ")
    with st.form(key='add_Order_Item_form'):
        order_id = st.number_input("Order Id", min_value=0, step=1)
        product_id = st.number_input("Product Id", min_value=0, step=1)
        quantity = st.number_input("Quantity", min_value=0, step=1)
        subtotal = st.number_input("Sub Total", min_value=0.0, step=0.01)
        #Submit Button For Adding New Order Items
        submit_button = st.form_submit_button("Add Order Item")
        #IF Button Pressed then Validate and Add Orders Items
        if submit_button:
            add_order_item(order_id, product_id, quantity, subtotal)
            st.success("Order Item added successfully!")
            display_order_items()

    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #update Orders Items Form
    st.subheader("Update Orders Items")
    st.write(" ")
    #Get Order Item Values in Form
    with st.form(key='update_Order_Item_form'):
        order_item_id = st.number_input("Order Item Id", min_value=0, step=1)
        quantity = st.number_input("Quantity", min_value=0, step=1)
        subtotal = st.number_input("Sub Total", min_value=0.0, step=0.01)
        submit_button = st.form_submit_button("Update Order Item")
        #IF Button Pressed then Update the Order ITems
        if submit_button:
            add_order_item(order_id, product_id, quantity, subtotal)
            st.success("Order Items updated successfully!")
            display_order_items()
    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    # TO Delete the Order Items
    st.subheader("Delete Order Items")
    st.write(" ")
    #Get the Order item Id to Delete
    order_item_id_to_delete = st.number_input("Order Item ID to Delete", min_value=1, step=1)
    #If Order Item id and Button Pressed then Delete Order Item
    if st.button("Delete Order"):
        delete_order_item(order_item_id_to_delete)
        st.success(f"Order {order_item_id_to_delete} deleted successfully!")
        #display Order items
        display_orders()



#if Sales Trend Page is SElected
elif page == "Sales Trend":
    #Title as Sales Trends
    st.subheader("Sales Trend")
    st.markdown("---")
    #for Sales of TOp Product BAr chart
    st.markdown("__Sales Trends for Top  Products__")
    st.write(" ")
    # Display Top Products
    display_sales_trend()
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #For Top Customers
    st.markdown("__Sales Trends for Top  Customers__")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #Display Bar chart for Top Customers
    display_top_Customer()
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #Sales for Orders of Specific Date Range
    st.markdown("__Sales Trend for Datewise Orders__")
    st.write(" ")
    #Display Pie Chart for Orders with Date Range
    display_Orders_Date()
    st.write(" ")
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    #Sales For Customer Product Spending
    st.markdown("__Sales Trend for Spending Category__")
    st.write(" ")
    st.write(" ")
    #Display Horizontal Chart for Customer Product Spending
    Customer_Spending_Category()

# run app using streamlit run DataMart.py