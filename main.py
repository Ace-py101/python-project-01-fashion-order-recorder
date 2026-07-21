from datetime import datetime


def display_menu():
  while True:
    print("=" * 35)
    print("FASHION HOUSE MANAGER")
    print("=" * 35)
    print("1. Create Order")
    print("2. Measurements")
    print("3. Styles")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
      create_order()

    elif choice == "2":
      print("Measurements feature coming soon")

    elif choice == "3":
      print("Styles feature coming soon")

    elif choice == "4":
      print("Goodbye!")
      break   

    else:
      print("Invalid option, please try again \n")
      
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
      print("Customer name must contain at least 3 letters.")
      continue

    customer_name = " ".join(customer_name.split())
    return customer_name

def get_phone_number():
  while True:
    phone_number = input("Enter phone number: ").strip()

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
      print("Garment type must contain at least 3 letters.")
      continue

    garment_type = " ".join(garment_type.split())
    return garment_type

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

        print("Deposit must be greater than zero and cannot exceed the price.")

    except ValueError:
      print("Please enter numbers only.")

def display_receipt(
    customer_name,
    phone_number,
    garment_type,
    quantity,
    delivery_date,
    price,
    deposit,
    balance,
):
    print("=" * 30)
    print("      START OF ORDER")
    print("=" * 30)

    print("Customer Name  :", customer_name)
    print("Phone Number   :", phone_number)
    print("Garment Type   :", garment_type)
    print("Quantity       :", quantity)
    print("Delivery Date  :", delivery_date)
    print("Price          : ₦", price)
    print("Deposit        : ₦", deposit)
    print("Balance        : ₦", balance)

    print("=" * 30)
    print("       END OF ORDER")
    print("Thanks for your patronage!")
    print("=" * 30)

def create_order():
    customer_name = get_customer_name()
    phone_number = get_phone_number()
    garment_type = get_garment_type()
    quantity = get_quantity()
    delivery_date = get_delivery_date()
    price = get_price()
    deposit = get_deposit(price)

    balance = price - deposit

    display_receipt(
        customer_name,
        phone_number,
        garment_type,
        quantity,
        delivery_date,
        price,
        deposit,
        balance,
    )

    save_order(
        customer_name,
        phone_number,
        garment_type,
        quantity,
        delivery_date,
        price,
        deposit,
        balance,
    )

    print("Order saved successfully.")

def save_order(
  customer_name,
  phone_number,
  garment_type,
  quantity,
  delivery_date,
  price,
  deposit,
  balance,
):
  with open("orders.txt", "a") as file:
    file.write("==============================\n")
    file.write("ORDER START\n")
    file.write("==============================\n")
    file.write(f"Customer Name : {customer_name}\n")
    file.write(f"Phone Number  : {phone_number}\n")
    file.write(f"Garment Type  : {garment_type}\n")
    file.write(f"Quantity      : {quantity}\n")
    file.write(f"Delivery Date : {delivery_date}\n")
    file.write(f"Price         : ₦{price}\n")
    file.write(f"Deposit       : ₦{deposit}\n")
    file.write(f"Balance       : ₦{balance}\n")
    file.write("==============================\n")
    file.write("ORDER END\n")
    file.write("Thanks for your patronage!\n")
    file.write("==============================\n\n")

def main():
  display_menu()

main()
