# Fashion House Order Recorder

## Project Description

This is a beginner Python project that records a fashion customer's order and prints a simple receipt.

## Features

- Collects customer name
- Collects phone number
- Collects garment type
- Collects quantity
- Collects delivery date
- Collects price
- Collects deposit
- Calculates remaining balance
- Prints a formatted receipt
- Collects customer details
- Calculates remaining balance
- Prints a formatted receipt
- Validates price input
- Prevents zero or negative prices
- Validates deposit input
- Prevents deposits greater than the total price
- Validates quantity input
- Validates price input
- Validates deposit input
- Handles invalid input using try/except
- Prevents negative or zero values
- Prevents deposit greater than the total price
- Collects customer details.
- Validates customer name.
- Validates phone number.
- Validates quantity.
- Validates price.
- Validates deposit amount.
- Displays a receipt after collecting information.

## Technologies Used

- Python 3
- Termux
- Git
- GitHub

## How to Run

```bash
python main.py
```

## What I Learned

- Variables
- User input using input()
- Integers using int()
- print()
- Basic arithmetic
- Storing values in variables
- Calculating balance
- while True loops
- try/except for error handling
- ValueError exception
- break statement
- Input validation
- Logical operators (or)
- Input validation
- `while` loops
- `if` statements
- String methods
- Error handling
- Debugging
- Basic problem-solving

## Customer Name Validation

- Cannot be empty.
- Must contain only letters and spaces.
- Minimum of 3 letters.
- Removes unnecessary spaces.
- Automatically capitalizes each word.

## Phone Number Validation

- Cannot be empty.
- Must contain only digits.
- Must be exactly 11 digits.
- Must start with `0`.

### Garment Type Validation

The application validates garment type by ensuring that:

- The input is not empty.
- Only letters and spaces are allowed.
- The input contains at least 3 letters.
- Extra spaces are removed automatically.
- Each word is automatically capitalized.

### Delivery Date Validation

The application validates the delivery date by ensuring that:

- The field is not empty.
- The date is entered in `DD/MM/YYYY` format.
- Invalid dates are rejected.
- The user is prompted again until a valid date is entered.

## New Feature: Save Orders to File

The application now automatically saves every completed customer order to a text file (`orders.txt`).

### Implementation

```python
with open("orders.txt", "a") as file:
    file.write(...)
    ```

    ### What is Saved

    - Customer Name
    - Phone Number
    - Garment Type
    - Quantity
    - Delivery Date
    - Price
    - Deposit
    - Balance

    Each new order is appended to the end of the file, preserving all previous records.


## Project Description

Fashion House Order Recorder is a Python-based application designed to help record customer garment orders.

The project demonstrates practical programming concepts including input validation, file handling, exception handling and modular programming.

The application is being developed with future expansion in mind, including conversion into a web-based management system.

---

## Features

- Interactive menu-driven interface.
- Create new customer orders.
- Validate customer names.
- Validate phone numbers.
- Validate garment types.
- Validate order quantity.
- Validate delivery dates.
- Validate price and deposit values.
- Automatically calculate customer balance.
- Display order receipt.
- Save completed orders to a text file.

---

## Current Program Structure

The project was refactored into reusable functions:

# Fashion House Order Recorder

A Python command-line application for managing fashion house orders.

This project is part of my Python learning journey and is being developed incrementally before being converted into a web application.

## Features

### Main Menu

- Orders
- Measurements (Coming Soon)
- Styles (Coming Soon)
- Exit

### Orders Menu

- Create Order
- View Orders
- Search Order
- Edit Order (Basic Version)
- Delete Order (Basic Version)
- Back

## Current Capabilities

### Create Order

Collects:

- Customer Name
- Phone Number
- Garment Type
- Quantity
- Delivery Date
- Price
- Deposit

Automatically calculates:

- Balance

Displays a receipt before saving the order.

### View Orders

Displays every saved order from `orders.txt`.

### Search Order

Allows searching for orders by customer name.

### Edit Order (Basic)

Allows searching for an existing order and updating selected information.

> This is currently a text-file implementation and will be improved after migrating to SQLite.

### Delete Order (Basic)

Allows deleting an order after confirmation.

> This feature will also be improved after the SQLite migration.

## Input Validation

The application validates:

- Customer name
- Phone number
- Garment type
- Quantity
- Delivery date
- Price
- Deposit

## Technologies

- Python 3
- File Handling
- Functions
- Loops
- Exception Handling
- Modular Programming

## Project Structure

```
main.py
orders.txt
README.md
learning_notes.md
```

## Future Improvements

- SQLite database
- Flask Web Application
- HTML/CSS Interface
- Search by phone number
- Customer management
- Measurements module
- Styles module
- Reports dashboard
- Edit individual fields
- Better user interface
- Authentication/Login

Fashion House Manager

A Python-based order management application designed for a fashion house workflow.

The project started as a simple terminal program for recording customer orders and has evolved into a modular application with validation, structured storage, and CRUD operations.

---

Features

Order Management

The application currently supports:

- Create new customer orders
- View all saved orders
- Search for specific orders
- Edit existing orders
- Delete orders

---

Current Project Structure

python-project-01-fashion-order-recorder/

├── main.py
├── orders.py
├── validation.py
├── receipt.py
├── storage.py
├── orders.json
├── README.md
├── learning_notes.md
└── pseudocode.txt

---

File Responsibilities

main.py

Responsible for:

- Starting the application
- Displaying the main menu
- Controlling navigation between features

---

orders.py

Contains the main order business logic:

- Creating orders
- Searching orders
- Editing orders
- Deleting orders

This file communicates with validation and storage modules.

---

validation.py

Responsible for checking user input.

Current validations include:

- Customer name validation
- Phone number validation
- Garment type validation
- Quantity validation
- Delivery date validation
- Price validation
- Deposit validation

The purpose is to prevent incorrect data from entering the system.

---

receipt.py

Handles customer receipt display.

It formats completed orders into a readable terminal receipt.

---

storage.py

Responsible for data persistence.

Current storage method:

- JSON file storage

Functions include:

- Loading saved orders
- Saving new orders
- Updating stored orders

---

Data Storage

The project originally used a text file:

orders.txt

Example:

Customer Name : Ace
Phone Number  : 07014287325
Price         : ₦15000

This worked for displaying information but was difficult to search, update, and manipulate.

The project was later migrated to JSON storage:

orders.json

Example:

[
    {
        "customer_name": "Ade",
        "phone_number": "07073770790",
        "garment_type": "Shirts",
        "quantity": 2,
        "delivery_date": "10/10/2029",
        "price": 50000,
        "deposit": 40000,
        "balance": 10000
    }
]

Advantages of JSON storage:

- Structured data
- Easier searching
- Easier editing
- Easier deletion
- Easier migration to databases later

---

CRUD Operations

The application now follows the CRUD pattern.

Create

Creates new orders and saves them into "orders.json".

Function:

create_order()

---

Read

Retrieves saved orders.

Functions:

view_orders()
search_order()

---

Update

Changes existing order information.

Function:

edit_order()

---

Delete

Removes existing orders.

Function:

delete_order()

---

Technologies Used

- Python
- JSON
- Git
- GitHub
- Termux Linux environment

---

Development Journey

Stage 1: Basic Python Program

Started with:

- Input/output
- Variables
- Conditions
- Loops
- Functions

---

Stage 2: Input Validation

Added protection against invalid information:

Examples:

- Empty names
- Invalid phone numbers
- Wrong dates
- Negative prices

---

Stage 3: Modular Refactoring

The original single Python file was divided into multiple modules.

Benefits:

- Cleaner code
- Easier maintenance
- Better organization
- Separation of responsibilities

---

Stage 4: JSON Migration

Moved from text storage to structured JSON storage.

This introduced concepts used in backend development:

- Serialization
- Deserialization
- Data persistence
- Structured records

---

Future Improvements

Planned features:

- Add unique order IDs
- Customer management module
- Measurements management
- Style catalogue
- Reports and analytics
- SQLite database integration
- Web application interface

---

Purpose

This project is a practical learning project focused on applying Python programming concepts to solve a real fashion business problem.

---

# Version 2.0 Update

This version introduces major improvements to the project architecture and data model.

## New Features

### Unique Order IDs

Every order now receives a unique identifier.

Example:

```json
{
    "order_id": 1001,
    "customer_name": "Ade",
    "phone_number": "07073770790"
}
```

Using Order IDs eliminates ambiguity when multiple customers have the same name and provides a reliable way to search, edit, and delete records.

---

### Improved CRUD Operations

All order operations now use **Order ID** instead of customer names.

Supported operations:

- Create Order
- View Orders
- Search Order by ID
- Edit Order by ID
- Delete Order by ID

This follows the same approach used in professional database-driven applications.

---

### Improved Data Model

Each order now contains:

- Order ID
- Customer Name
- Phone Number
- Garment Type
- Quantity
- Delivery Date
- Price
- Deposit
- Balance

This provides a structured and scalable record format.

---

### Safer Data Handling

The application now:

- Generates unique Order IDs automatically.
- Preserves existing orders during updates.
- Removes only the selected order during deletion.
- Stores data in structured JSON format.

---

# Current Architecture

```text
User
 │
 ▼
main.py
 │
 ▼
orders.py
 │
 ├── validation.py
 ├── receipt.py
 └── storage.py
          │
          ▼
     orders.json
```

---

# Project Status

Completed features:

- Main Menu
- Orders Menu
- Modular Project Structure
- Input Validation
- Receipt Generation
- JSON Storage
- Unique Order IDs
- Full CRUD Operations

Current storage technology:

- JSON

Next planned milestone:

- Flask Web Interface (MVP)

Future milestones:

- SQLite integration
- Customer module
- Measurements module
- Styles module
- Reports dashboard
- Production deployment
