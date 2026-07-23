# Learning Notes
## Project 1: Fashion House Order Recorder

### Date
July 2026

---

## Concepts I Learned

### 1. Problem Solving Workflow

I learned that software development follows a process:

1. Understand the problem.
2. Write the pseudocode.
3. Write the Python code.
4. Run and test the program.
5. Refactor (improve the code).
6. Commit to GitHub.
7. Write documentation.

---

### 2. Variables

A variable is a named container that stores a value.

Example:

customer_name = "Oluwatobi"

The variable is `customer_name`.
The value stored in it is `"Oluwatobi"`.

---

### 3. User Input

I learned how to collect information from users using `input()`.

Example:

customer_name = input("Enter customer's name: ")

---

### 4. Data Types

I learned that:

- Strings (`str`) store text.
- Integers (`int`) store whole numbers.

Examples:

price = 50000
customer_name = "Oluwatobi"

---

### 5. Why Phone Numbers Are Strings

Although phone numbers contain digits, they are identifiers, not numbers for calculations.

Therefore:

phone_number = input("Enter phone number: ")

---

### 6. Expressions

An expression produces a value.

Example:

price - deposit

---

### 7. Assignment

Assignment stores a value in a variable.

Example:

balance = price - deposit

---

### 8. Printing

I learned how to display variables using `print()`.

Example:

print("Customer Name:", customer_name)

---

### 9. Difference Between Variable and Text

Without quotation marks:

print(customer_name)

prints the value stored in the variable.

With quotation marks:

print("customer_name")

prints the text "customer_name".

---

### 10. Variables Can Change

Variables do not remember previous values.

Example:

price = 50000
price = 70000

The value becomes 70000.

---

### 11. Calculations Are Not Automatic

After calculating:

balance = price - deposit

Changing `deposit` later does not automatically change `balance`.

I must calculate it again.

---

### 12. Linux Commands Learned

mkdir  - Create a directory
cd     - Change directory
ls     - List files and folders
touch  - Create a file
mv     - Rename or move files/folders
cat    - Display file contents
micro  - Edit files

---

## Mistakes I Made

- I thought Python code using `input()` was pseudocode.
- I used `cd` on a file instead of a directory.
- I misspelled "recorder" in my project folder.
- I wrote `pythonmain.py` instead of `python main.py`.
- I accidentally indented `print()` and got an IndentationError.
- I entered `N100000` instead of `100000`, causing a ValueError.
- I printed `"customer_name"` instead of the value stored in `customer_name`.

---

## Questions I Asked

- What is pseudocode?
- What is hardcoding?
- Why are phone numbers stored as strings?
- What is the difference between a variable and its value?
- What is the difference between an expression and an assignment statement?
- Why write pseudocode before writing Python code?

---

## What I Am Proud Of

- I wrote my first Python project myself.
- I created and organized a real project folder.
- I used Git and Linux commands in Termux.
- I learned to read and fix Python errors instead of giving up.

---

## New Vocabulary

- Variable
- String
- Integer
- Expression
- Assignment
- Statement
- Pseudocode
- Hardcoding
- Repository
- Commit

## Goal for Project 2

Learn how to make decisions in Python using `if` statements and improve the Fashion House Order Recorder with input validation.

## Update 1 - Input Validation

### New Concept: while Loop for Validation

A `while` loop keeps running as long as its condition is True.

Example:

```python
while price <= 0:
    print("Price must be greater than zero.")
    price = int(input("Enter Price: "))

        ## What I Learned
- Variables
- User input with `input()
- Integer conversion using `int()`
- Basic arithmetic
- Input validation
- `while` loops
- Logical operators (`or`)
- Preventing invalid user input
- Avoiding infinite loops

## Update 1.1 - Input Validation

Today I improved my Fashion House Order Recorder by adding proper input validation.

Concepts learned:

- while True creates a loop that keeps asking until valid input is entered.
- try catches code that may raise an error.
- except ValueError handles invalid inputs such as letters or symbols when an integer is expected.
- break immediately exits the loop once valid input is received.
- The loop continues automatically after an exception unless break is reached.
- The "or" logical operator allows checking multiple conditions in one statement.
- Business rules can also be validated, such as:
- Price must be greater than zero.
- Quantity must be at least 1.
- Deposit must be greater than zero.
- Deposit cannot be greater than the total price.

This made the program much more reliable and user-friendly.

# Update 2

## Customer name and phone number validation 

### What I learned

- How to use `while True` loops for input validation.
- How `continue` asks the user for input again when validation fails.
- How `break` exits a loop only after all validation checks pass.
- The difference between syntax errors and logic errors.
- How to read Python error messages and use them to debug my code.
- How to validate string input using:
- `strip()`
- `replace()`
- `isalpha()`
- `isdigit()`
- `startswith()`
- `title()`
- `split()`
- `" ".join()`
- The difference between `==` (equal to) and `!=` (not equal to).
- The importance of indentation in Python.

## Validation added

 ### Customer Name
- Cannot be empty.
- Must contain only letters and spaces.
- Must contain at least 3 letters.
- Automatically removes extra spaces.
- Automatically capitalizes each word.

 ### Phone Number
- Cannot be empty.
- Must contain only digits.
- Must be exactly 11 digits.
- Must start with `0`.

## Problems I solved

- Fixed `AttributeError` caused by writing `startwith()` instead of `startswith()`.
- Fixed `SyntaxError` caused by using `! =` instead of `!=`.
- Fixed missing parentheses in `len()` validation.
- Fixed a logic error where an invalid phone number was accepted because I forgot to use `continue`.
                
## Garment Type Validation

### Validation Added

- Garment type cannot be empty.
- Garment type must contain only letters and spaces.
- Garment type must contain at least 3 letters.
- Removes unnecessary spaces between words.
- Automatically capitalizes the first letter of each word.

### What I Learned

- Similar validation logic can be reused for different text inputs.
- The combination of `split()`, `" ".join()`, and `title()` helps clean and format user input.
- Using `continue` ensures invalid input is rejected and the user is prompted again.


## Delivery Date Validation

### Validation Added

- Delivery date cannot be empty.
- Delivery date must follow the `DD/MM/YYYY` format.
- Invalid dates are rejected.
- The user is prompted again until a valid date is entered.

### New Concept Learned

- Imported Python's built-in `datetime` module.
- Used `datetime.strptime()` to validate dates.
- Used a `try`/`except` block to catch invalid date entries.

### What I Learned

- Python provides built-in modules that simplify complex tasks.
- `datetime.strptime()` checks both the date format and whether the date actually exists.
- Validation becomes more reliable when using standard library modules instead of writing custom logic.

## File Handling - Saving Orders

### Opening a File

```python
with open("orders.txt", "a") as file:
```

- `with` automatically closes the file after use.
- `"orders.txt"` is the file name.
- `"a"` means **append mode**, which adds new data without deleting existing records.

### Writing to a File

```python
file.write(f"Customer Name : {customer_name}\n")
```

- `file.write()` writes text to the file.
- `f""` (formatted string) inserts variable values into the text.
- `\n` creates a new line.

### Key Learning

- Save program output permanently.
- Append new records instead of overwriting existing ones.
- Store formatted customer receipts in a text file.
- Use file handling to keep records after the program closes.

# Learning Notes

## Project Refactoring

Today I refactored my Fashion House Order Recorder project from a single long procedural script into a cleaner function-based application.

## What I Learned

### Functions

- How to create reusable functions using `def`.
- Functions should have one responsibility and perform a specific task.
- How to pass data into functions using parameters.
- How functions return values using `return`.
- The difference between parameters and arguments.

### Variables, Parameters and Constants

- Variables store data that can change during program execution.
- Parameters are variables created inside a function definition to receive data.
- Arguments are the actual values passed into a function when calling it.
- Constants are values that should remain unchanged throughout the program.

### Input Validation

I separated input validation into individual functions:

- `get_customer_name()`
- `get_phone_number()`
- `get_garment_type()`
- `get_quantity()`
- `get_delivery_date()`
- `get_price()`
- `get_deposit()`

Each function:
1. Collects user input.
2. Checks if the input is valid.
3. Returns the correct value.

### Exception Handling

I learned that `try/except` is used to handle errors that may occur while a program is running.

Examples:

- `ValueError` when converting invalid input to integers.
- `FileNotFoundError` when trying to open a missing file.
- `KeyError` when accessing a missing dictionary key.

I also learned that not every validation requires `try/except`. Conditions that can be checked directly should use `if` statements.

Example:

```python
if customer_name == "":
    print("Customer name cannot be empty.")

# Learning Notes

## Refactoring

Refactored the application into small reusable functions instead of writing everything inside one large script.

Examples:

- display_menu()
- order_menu()
- create_order()
- display_receipt()
- save_order()

Benefits:

- Cleaner code
- Easier debugging
- Easier maintenance
- Better preparation for Flask

---

## Modular Programming

Instead of repeating code, each task should have its own function.

One function should perform one responsibility.

Example:

create_order() collects data.

display_receipt() prints the receipt.

save_order() saves data to the file.

---

## Nested Menu System

Implemented a two-level menu.

Main Menu

```
Orders
Measurements
Styles
Exit
```

Orders Menu

```
Create Order
View Orders
Search Order
Edit Order
Delete Order
Back
```

This structure makes the application easier to expand.

---

## CRUD Operations

Learned the four basic operations used in most software systems.

Create

Create new order.

Read

View Orders

Search Orders

Update

Edit Order (Basic)

Delete

Delete Order (Basic)

These operations form the foundation of management systems.

---

## View Orders

Learned how to:

- Open a file
- Read file contents
- Display saved records
- Handle FileNotFoundError

---

## Search Order

Learned:

- String searching
- .lower()
- .strip()
- Case-insensitive searching

Example:

```
"Ace".lower()
```

Returns

```
ace
```

---

## Edit Order

Built the first version of editing records.

Learned:

- Read entire file
- Split records
- Rewrite file
- Replace text
- Update data

Current implementation works but will be redesigned after migrating to SQLite.

---

## Delete Order

Built a basic delete feature.

Concept learned:

Instead of deleting directly from the file,

Read all records

↓

Keep only records that should remain

↓

Rewrite the file

This introduced the concept of rebuilding a file after removing unwanted records.

---

## File Modes

Learned the purpose of different file modes.

```
"r"  Read

"w"  Write (overwrite)

"a"  Append
```

---

## Lists

Used lists to temporarily store records while editing and deleting.

Methods learned:

- append()

Functions learned:

- split()
- join()

---

## String Methods

Practiced:

- replace()
- strip()
- lower()
- startswith()
- isalpha()
- isdigit()

---

## Loops

Used:

- while loops
- for loops

while

Used for repeated user input until valid.

for

Used for processing every saved order.

---

## Exception Handling

Used try/except to handle:

- Invalid numeric input
- Missing files

Examples:

- ValueError
- FileNotFoundError

---

## Software Design Lesson

Text files are suitable for learning file handling but become difficult for searching, editing and deleting records.

SQLite provides a better solution because data is stored in structured tables instead of plain text.

This project will migrate from:

orders.txt

to

orders.db

before building the Flask web application.

---

## Next Milestone

- SQLite Database
- Connect Python to SQLite
- Store orders in database
- Replace text-file CRUD with database CRUD
- Build Flask Web Application
