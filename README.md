# 📦 Mini E-Commerce Web App (Flask + Excel)

A beginner-friendly Flask web application for a mini e-commerce system where data is stored in an Excel file (data_new.xlsx) instead of a database.

## 🚀 Features

Users (Customers)

Register/Login

Browse products

Place orders

Seller

Fixed login (seller / seller123)

Add new products

Update stock and price

Admin

Fixed login (admin / admin123)

View/manage all users, products, and orders

## 📂 Project Structure
ECOMMERCE_APP/
│── app.py               # Main entry point
│── requirements.txt     # Dependencies
│── data_new.xlsx        # Excel file (database with 3 sheets)
│── README.md            # Documentation
│
├── routes/              # All routes
│   ├── users/users.py       # Register, login, dashboard
│   ├── products/products.py # Product management
│   └── orders/orders.py     # Order management
│
├── templates/           # HTML (Bootstrap styled)
    ├── base.html
    ├── users/           # register.html, login.html, dashboard.html
    ├── products/        # products.html
    └── orders/          # orders.html

## 🗂️ Excel Database (data_new.xlsx)

The project uses Excel sheets as database tables:

Users → UserID, Username, Password, Email, Role

Products → ProductID, Name, Price, Stock, SellerID

Orders → OrderID, UserID, ProductID, Quantity, OrderDate

## ⚙️ Installation

Clone the repository (or copy files).

Install dependencies:

pip install -r requirements.txt


Ensure you have an Excel file named data_new.xlsx with 3 empty sheets: Users, Products, Orders.

Example headers:

Users → UserID | Username | Password | Email | Role

Products → ProductID | Name | Price | Stock | SellerID

Orders → OrderID | UserID | ProductID | Quantity | OrderDate

Run the app:

python app.py


Open in browser:
👉 http://127.0.0.1:5000/

## 🔑 Credentials

Admin → admin / admin123

Seller → seller / seller123

Customer → Register first, then login with your details

## 📖 How It Works

Customer registers → Data saved in Users sheet.

Customer logs in → Sees products from Products sheet.

Customer places an order → Stock decreases in Products, new row added in Orders.

Seller logs in → Can add/update products (reflected in Products sheet).

Admin logs in → Can view all users, products, and orders.

## 🎨 UI

Built with Bootstrap 5 for a simple, clean e-commerce look.

Product listing → Cards with order/update forms.

Orders → Displayed in a styled table.

✅ That’s it — a simple but functional Excel-powered e-commerce web app for learning Flask!
