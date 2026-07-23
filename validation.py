from datetime import datetime


def get_customer_name():
    while True:
        customer_name = input("Enter customer name: ")

        if customer_name == "":
            print("Customer name cannot be empty.")
            continue

        if not customer_name.replace(" ", "").isalpha():
            print("Customer name can only contain letters.")
            continue

        if len(customer_name.replace(" ", "")) < 3:
            print("Customer name must contain at least 3 characters.")
            continue

        customer_name = " ".join(customer_name.split())

        return customer_name.title()


def get_phone_number():
    while True:
        phone_number = input("Enter phone number: ")

        if phone_number == "":
            print("Phone number cannot be empty.")
            continue

        if not phone_number.isdigit():
            print("Phone number can only contain numbers.")
            continue

        if len(phone_number) != 11:
            print("Phone number must be exactly 11 digits.")
            continue

        if not phone_number.startswith("0"):
            print("Phone number must start with 0.")
            continue

        return phone_number


def get_garment_type():
    while True:
        garment_type = input("Enter garment type: ")

        if garment_type == "":
            print("Garment type cannot be empty.")
            continue

        if not garment_type.replace(" ", "").isalpha():
            print("Garment type can only contain letters.")
            continue

        if len(garment_type.replace(" ", "")) < 3:
            print("Garment type must contain at least 3 characters.")
            continue

        garment_type = " ".join(garment_type.split())

        return garment_type.title()


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity >= 1:
                return quantity

            print("Quantity cannot be less than 1.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def get_delivery_date():
    while True:
        delivery_date = input("Enter delivery date (DD/MM/YYYY): ")

        if delivery_date == "":
            print("Delivery date cannot be empty.")
            continue

        try:
            datetime.strptime(delivery_date, "%d/%m/%Y")
            return delivery_date

        except ValueError:
            print("Please enter the date in DD/MM/YYYY format.")


def get_price():
    while True:
        try:
            price = int(input("Enter price: "))

            if price > 0:
                return price

            print("Price must be greater than zero.")

        except ValueError:
            print("Please enter numbers only.")


def get_deposit(price):
    while True:
        try:
            deposit = int(input("Enter deposit: "))

            if deposit > 0 and deposit <= price:
                return deposit

            print("Deposit must be greater than zero and not exceed price.")

        except ValueError:
            print("Please enter numbers only.")
