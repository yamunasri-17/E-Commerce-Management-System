import mysql.connector

# CONNECT DB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yamu",
    database="e_commerce"
)
cursor = conn.cursor()

print("Connected Successfully")

# ---------------- LOGIN ----------------
def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    query = "SELECT * FROM Users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    if user:
        print("Login Successful")
        return user[0]   # user_id
    else:
        print("Invalid Credentials")
        return None

# ---------------- VIEW PRODUCTS ----------------
def view_products():
    print("\n--- PRODUCT LIST ---\n")
    cursor.execute("SELECT product_id, product_name, price FROM Products")

    for row in cursor.fetchall():
        print(row)

# ---------------- ADD TO CART ----------------
def add_to_cart(user_id):
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))

    query = "INSERT INTO Cart (user_id, product_id, quantity) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, product_id, quantity))
    conn.commit()

    print("Added to cart")

# ---------------- VIEW CART ----------------
def view_cart(user_id):
    query = """
    SELECT p.product_name, c.quantity, p.price
    FROM Cart c
    JOIN Products p ON c.product_id = p.product_id
    WHERE c.user_id = %s
    """

    cursor.execute(query, (user_id,))

    for row in cursor.fetchall():
        print(row)

# ---------------- PLACE ORDER ----------------
def place_order(user_id):
    cursor.execute("SELECT product_id, quantity FROM Cart WHERE user_id=%s", (user_id,))
    cart_items = cursor.fetchall()

    total_amount = 0

    for item in cart_items:
        product_id, quantity = item

        cursor.execute("SELECT price FROM Products WHERE product_id=%s", (product_id,))
        price = cursor.fetchone()[0]

        total_amount += price * quantity

    cursor.execute("INSERT INTO Orders (user_id, total_amount) VALUES (%s, %s)", (user_id, total_amount))
    conn.commit()

    order_id = cursor.lastrowid
    print("Order ID:", order_id)

    for item in cart_items:
        product_id, quantity = item

        cursor.execute("SELECT price FROM Products WHERE product_id=%s", (product_id,))
        price = cursor.fetchone()[0]

        cursor.execute(
            "INSERT INTO Order_Items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
            (order_id, product_id, quantity, price)
        )

    conn.commit()
    print("Order Placed Successfully")

# ---------------- PAYMENT ----------------
def payment():
    order_id = int(input("Enter order ID: "))
    amount = int(input("Enter amount: "))
    method = input("Enter method (UPI/Card/Cash): ")

    # Ensure there are EXACTLY 4 '%s' for the 4 values in the tuple
    query = "INSERT INTO Payments (order_id, amount, payment_method, status) VALUES (%s, %s, %s, %s)"
    
    # Ensure the tuple contains exactly: (order_id, amount, method, "Success")
    cursor.execute(query, (order_id, amount, method, "Success"))
    conn.commit()
    print("Payment Successful")

# ---------------- ORDER HISTORY ----------------
def order_history(user_id):
    query = "SELECT * FROM Orders WHERE user_id=%s"
    cursor.execute(query, (user_id,))

    for row in cursor.fetchall():
        print(row)

# ---------------- MAIN MENU ----------------
user_id = login()

if user_id:
    while True:
        print("\n1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Payment")
        print("6. Order History")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            view_products()
        elif choice == 2:
            add_to_cart(user_id)
        elif choice == 3:
            view_cart(user_id)
        elif choice == 4:
            place_order(user_id)
        elif choice == 5:
            payment()
        elif choice == 6:
            order_history(user_id)
        elif choice == 7:
            break