# Store Management System

A Python-based Store Management System designed as Project 4 of my Python learning path.

This project focuses on building a more realistic software system using Object-Oriented Programming and gradually introducing concepts that are useful for backend development.

## 🎯 Project Goal

The goal of this project is to build a store management system where products, customers, and orders can be managed through a structured Python application.

The project is designed to strengthen:

* Object-Oriented Programming
* Class design
* Inheritance
* Business Logic
* Error handling
* Regular Expressions
* HTTP Requests
* Web Scraping
* Clean project structure
* Git and GitHub workflow

The project will also become the foundation for a future version that uses SQL, a real database, and an API.

## 🏗️ Project Architecture

The current design contains five main classes:

```text
Product
Customer
OrderItem
Order
Store
```

### Product

Represents a product available in the store.

Main attributes:

```text
product_id
name
stock
price
expiration_date
```

### Customer

Represents a customer.

Main attributes:

```text
customer_id
name
balance
phone
```

### OrderItem

Represents one item inside an order.

For example:

```text
Mouse × 2
Keyboard × 1
Headphone × 3
```

Main attributes:

```text
product
quantity
subtotal
```

### Order

Represents a complete customer order.

Main attributes:

```text
order_id
customer
items
total_price
date
status
```

An order can contain multiple `OrderItem` objects.

### Store

The main class responsible for the store's business logic.

Main attributes:

```text
products
customers
orders
balance
commission_rate
```

## 🔗 Relationships

The main relationships between the classes are:

```text
Store
 ├── Products
 ├── Customers
 └── Orders

Customer
 └── Orders

Order
 ├── Customer
 └── OrderItems

OrderItem
 └── Product
```

## 🛒 Order System

A customer can purchase multiple products in a single order.

For example:

```text
Mouse       × 2
Keyboard    × 1
Headphone   × 1
Flash Drive × 3
```

All of these products belong to one `Order`.

The system calculates the subtotal of each `OrderItem` and then calculates the total price of the entire order.

## 💰 Purchase Business Logic

Before completing an order, the system checks all required conditions.

The general flow is:

```text
Customer selects products
        ↓
Create Order
        ↓
Check all product stocks
        ↓
Calculate total price
        ↓
Check customer balance
        ↓
Complete purchase
        ↓
Reduce product stocks
        ↓
Reduce customer balance
        ↓
Calculate store commission
        ↓
Increase store balance
        ↓
Save Order
```

If any required condition fails, the order should not be completed.

## 📦 Stock Validation

If a customer requests more products than are available, the order is rejected.

Example:

```text
Requested: 5 headphones
Available: 2 headphones
```

Result:

```text
Order rejected
```

No product stock or customer balance should be changed.

## 💳 Customer Balance

The customer must have enough balance to pay for the entire order.

Example:

```text
Order total:       5,000,000
Customer balance:  3,000,000
```

The purchase is rejected because the customer's balance is insufficient.

## 🏦 Store Balance and Commission

The store has its own balance.

A commission rate can be defined for each sale.

For example:

```text
Order total = 1,000,000
Commission = 5%
```

The store receives:

```text
950,000
```

The commission logic can later be expanded into a more complete financial system.

## ❌ Order Cancellation

The project will also support order cancellation.

When an order is successfully cancelled, the system may:

* Restore product stock
* Return the customer's payment
* Update the store balance
* Change order status to `Cancelled`

Cancellation rules will be defined during implementation.

## 🌐 Web Scraping

One of the main features of Project 4 is importing product information from public web pages.

The planned flow is:

```text
URL
 ↓
Requests
 ↓
HTML
 ↓
Extract information
 ↓
Process data
 ↓
Create Product
 ↓
Add Product to Store
```

Regular Expressions and other appropriate Python techniques will be used when necessary.

Only publicly accessible and appropriate web pages should be used for the scraping exercises.

## 🧠 Learning Objectives

During this project I will practice thinking like a software developer rather than only solving isolated programming exercises.

Important questions during development include:

* What classes do I need?
* What responsibility belongs to each class?
* How are objects related?
* Where should business logic live?
* What should happen when an operation fails?
* How can I prevent inconsistent data?
* How can the project structure be improved?
* How can the system be extended later?

## 📁 Project Structure

The planned project structure is:

```text
Store-Management-System/
│
├── main.py
├── models.py
├── store.py
├── scraper.py
├── README.md
├── notes.txt
└── uml.txt
```

### File Responsibilities

#### `main.py`

Responsible for running the application and interacting with the user through the main menu.

#### `models.py`

Contains the main data models/classes:

```text
Product
Customer
OrderItem
Order
```

#### `store.py`

Contains the `Store` class and the main store business logic.

#### `scraper.py`

Contains the web scraping functionality using requests and data extraction techniques.

#### `notes.txt`

Contains personal learning notes, important concepts, challenges, bugs, and lessons learned during the project.

#### `uml.txt`

Contains the system architecture and class relationships.

## 🧪 Planned Main Menu

The exact menu may change during development, but the initial idea is:

```text
1. Add Product
2. Remove Product
3. Find Product
4. Show Products

5. Add Customer
6. Remove Customer
7. Find Customer
8. Show Customers

9. Create Order
10. Show Orders
11. Cancel Order

12. Import Product From Web

0. Exit
```

## 🚀 Future Development

This project is intentionally designed so that it can evolve into a more realistic backend project.

After completing the Python version, the same project can be upgraded instead of being discarded.

### Future Version

```text
Store Management System v1
        ↓
Python + OOP
        ↓
Regex + Requests + Web Scraping
        ↓
Store Management System v2
        ↓
SQL + Database
        ↓
Store Management System v3
        ↓
Backend API
```

The future database version will introduce concepts such as:

* SQL
* Database design
* Tables
* Primary Keys
* Foreign Keys
* Relationships
* CRUD operations
* Python Database connection

The API version will introduce:

* REST API concepts
* HTTP methods
* Endpoints
* JSON
* Request/Response
* Backend communication

## 📝 Development Philosophy

This project is not intended to be completed by writing all the code at once.

The development process will be:

```text
Requirements
    ↓
Design
    ↓
Architecture
    ↓
UML
    ↓
Implementation
    ↓
Testing
    ↓
Debugging
    ↓
Refactoring
    ↓
Documentation
```

New features will be added only when they have a clear purpose.

The goal is to understand the reason behind the code, not just make the program work.

## 📌 Current Status

### Completed

* Initial project idea
* Main requirements
* Initial class design
* Class relationships
* Order architecture
* Business rules
* UML design
* Project structure

### Next Steps

* Start implementing the classes
* Implement Product
* Implement Customer
* Implement OrderItem
* Implement Order
* Implement Store
* Build the main menu
* Add tests and handle errors
* Add Regex
* Add Requests
* Add Web Scraping
* Refactor and improve the project

## 🔥 Final Goal

The final goal of this project is not only to build a store management program.

It is to practice the mindset required to build larger software systems:

```text
Understand the problem
        ↓
Design the system
        ↓
Break the problem into components
        ↓
Implement
        ↓
Test
        ↓
Debug
        ↓
Improve
```

This project will later serve as the foundation for learning SQL, databases, APIs, and backend development.
