🛒 E-Commerce Console Application (Python + MySQL)

📌 Overview

This project is a console-based E-Commerce system developed using Python and MySQL. It allows users to browse products, manage a shopping cart, place orders, and complete payments through a simple command-line interface.


🚀 Features

👤 User Module

- User login authentication
- View available products
- Add products to cart
- View cart details
- Place orders
- Make payments
- View order history

🛠️ Admin Module

- Add new products
- Update product details
- Delete products


🏗️ Technologies Used

- Python
- MySQL
- MySQL Connector


🗂️ Database Structure

The system uses the following main tables:

- Users – Stores user login information
- Products – Contains product details like name, category, price, and stock
- Cart – Stores items added by users
- Orders – Maintains order records
- Order_Items – Stores products included in each order
- Payments – Tracks payment details


⚙️ Setup Instructions

1. Install the required MySQL connector for Python
2. Create a database named “e_commerce”
3. Create all necessary tables (Users, Products, Cart, Orders, Order_Items, Payments)
4. Update database connection details in the Python file (host, username, password)
5. Run the Python program


▶️ How It Works

1. User logs into the system
2. User views the list of available products
3. Products are added to the cart
4. Order is placed from the cart
5. Payment is completed
6. Order history can be viewed


🔮 Future Enhancements

- Add graphical interface using Tkinter
- Convert into a full-stack web application
- Implement secure password hashing
- Add product images and search functionality
- Improve validation and error handling


👩‍💻 Author

Yamuna Sri E


📜 Note

This project is developed for educational and learning purposes.
