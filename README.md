# E-commerce Admin Backend API

This project provides a backend API for managing categories products,inventory, sales, sale states and revnue for an e-commerce admin dashboard. 
It is built with **FastAPI** and uses **MySQL** for persistent storage.

##  Features

-  Product & Category Management
-  Inventory Tracking & Low Stock Alerts
-  Sales Analytics & Revenue Reports
-  Time-Based and Category-Based Filtering

---

### 1. Clone the Repository

#bash
git clone https://github.com/YOUR_USERNAME/fastapi-ecommerce-admin.git
cd fastapi-ecommerce-admin


### 1. Setup Instructions
 Dependencies
    FastAPI
    SQLAlchemy
    MySQL Connector
    Uvicorn
    MySQL Server

    mysql -u root -p
    ALTER USER 'youruser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
    FLUSH PRIVILEGES;
    Note: Don't forget to update user name and password in database.py file

  Installatioin(Move to project directory)
    Install python according to OS
    python3 -m venv .venv /python -m venv .venv(Create virtual Envirnament) 
    source .venv/bin/activate(It may vary for different OS)
    pip install fastapi,uvicorn,sqlalchemy,pymysql
    After starting application please execute sql scripts **/scripts/demo_ref_scripts.sql**
    DDL scrpts are also provided but no need to execute as at start of application tables will create
    

API Endpoints Overview

| Method | Endpoint                | Description                |
| ------ | ----------------------- | -------------------------- |
| GET    | `/category/`            | Get all categories         |
| POST   | `/category/`            | Add new a categories       |
| PUT    | `/category/`            | Update a categories        |
| GET    | `/products/`            | Get all products           |
| POST   | `/products/`            | Create a new product       |
| GET    | `/sales/summary/`       | Get sales summary          |
| GET    | `/sales/by-category/`   | Get revenue by category    |
| GET    | `/inventory/low-stock/` | Get low stock items        |
| PUT    | `/inventory/{id}`       | Update stock for a product |
| POST   | `/sales/record/`        | Record a new sale          |

More endpoints can be found in the documentation at:
Swagger UI: http://127.0.0.1:8000/docs#/

Upcoming features:
-Product Information update
-Pagination
-Sale States Generator
-Order by(ASC/DESC) fuctionality for different endopionts
-For get("./revneue") endpoint. New endpointh that will return priod options for admins screen
-Response vaidation
-Separate CRUD operation class

