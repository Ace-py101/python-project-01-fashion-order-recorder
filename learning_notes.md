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
