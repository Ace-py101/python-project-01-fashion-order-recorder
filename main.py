from datetime import datetime


def display_menu():
  while True:
    print("=" * 35)
    print("FASHION HOUSE MANAGER")
    print("=" * 35)
    print("1. Orders")
    print("2. Measurements")
    print("3. Styles")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
      order_menu()

    elif choice == "2":
      print("Measurements feature coming soon")

    elif choice == "3":
      print("Styles feature coming soon")

    elif choice == "4":
      print("Goodbye!")
      break   

    else:
      print("Invalid option, please try again \n")

def order_menu():
    while True:
        print("=" * 30)
        print("          ORDERS")
        print("=" * 30)
        print("1. Create Order")
        print("2. View Orders")
        print("3. Search Order")
        print("4. Edit Order")
        print("5. Delete Order")
        print("6. Back")

        choice = input("Select option: ")

        if choice == "1":
            create_order()

        elif choice == "2":
            view_orders()

        elif choice == "3":
            search_order()

        elif choice == "4":
            edit_order()

        elif choice == "5":
            delete_order()

        elif choice == "6":
            break

        else:
            print("Invalid option")
      
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

def view_orders():
    print("=" * 30)
    print("        ALL ORDERS")
    print("=" * 30)

    try:
        with open("orders.txt", "r") as file:
            orders = file.read()

            if orders == "":
                print("No orders found.")

            else:
                print(orders)

    except FileNotFoundError:
        print("No order record found.")

    print("=" * 30)

def search_order():
    print("=" * 30)
    print("       SEARCH ORDER")
    print("=" * 30)

    search_name = input("Enter customer name: ").strip()

    try:
        with open("orders.txt", "r") as file:
            orders = file.read()

            if search_name.lower() in orders.lower():
                print("Order found!")
                print("=" * 30)

                print(orders)

            else:
                print("No order found for this customer.")

    except FileNotFoundError:
        print("No order record found.")

    print("=" * 30)

def edit_order():
    print("=" * 30)
    print("        EDIT ORDER")
    print("=" * 30)

    search_name = input("Enter customer name: ").strip()

    try:
        with open("orders.txt", "r") as file:
            orders = file.read()

        order_list = orders.split("==============================\n\n")

        updated_orders = []

        found = False

        for order in order_list:

            if search_name.lower() in order.lower():

                found = True

                print("Order found.")
                print(order)

                new_garment = input("Enter new garment type: ")
                new_quantity = input("Enter new quantity: ")
                new_price = input("Enter new price: ")
                new_deposit = input("Enter new deposit: ")

                balance = int(new_price) - int(new_deposit)

                order = order.replace(
                    order,
                    f"""==============================
ORDER START
Customer Name : {search_name}
Garment Type  : {new_garment}
Quantity      : {new_quantity}
Price         : ₦{new_price}
Deposit       : ₦{new_deposit}
Balance       : ₦{balance}
ORDER END
"""
                )

            updated_orders.append(order)

        if found:
            with open("orders.txt", "w") as file:
                file.write("==============================\n\n".join(updated_orders))

            print("Order updated successfully.")

        else:
            print("Order not found.")

    except FileNotFoundError:
        print("No order record found.")

    print("=" * 30)
    
def delete_order():
    print("=" * 30)
    print("       DELETE ORDER")
    print("=" * 30)

    while True:
        customer_name = input("Enter customer name: ").strip()

        try:
            with open("orders.txt", "r") as file:
                orders = file.read()

            order_list = orders.split("==============================\n\n")

            remaining_orders = []
            found = False

            for order in order_list:

                if customer_name.lower() in order.lower():

                    found = True

                    print("\nOrder Found:\n")
                    print(order)

                    confirm = input(
                        "Delete this order? (Y/N): "
                    ).strip().lower()

                    if confirm == "y":
                        print("Order deleted successfully.")
                        continue

                    else:
                        remaining_orders.append(order)
                        print("Deletion cancelled.")
                        continue

                remaining_orders.append(order)

            if not found:
                print("Order not found.")
                retry = input(
                    "Try again? (Y/N): "
                ).strip().lower()

                if retry == "y":
                    continue
                else:
                    return

            with open("orders.txt", "w") as file:
                file.write(
                    "==============================\n\n".join(remaining_orders)
                )

            return

        except FileNotFoundError:
            print("No order record found.")
            return
              
def main():
  display_menu()

main()
