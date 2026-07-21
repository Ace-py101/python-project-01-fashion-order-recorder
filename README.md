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
