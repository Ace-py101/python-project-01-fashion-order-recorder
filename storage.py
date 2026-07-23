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
        file.write("=" * 30 + "\n")
        file.write("ORDER START\n")
        file.write("=" * 30 + "\n")

        file.write(f"Customer Name : {customer_name}\n")
        file.write(f"Phone Number  : {phone_number}\n")
        file.write(f"Garment Type  : {garment_type}\n")
        file.write(f"Quantity      : {quantity}\n")
        file.write(f"Delivery Date : {delivery_date}\n")
        file.write(f"Price         : ₦{price}\n")
        file.write(f"Deposit       : ₦{deposit}\n")
        file.write(f"Balance       : ₦{balance}\n")

        file.write("=" * 30 + "\n")
        file.write("ORDER END\n")
        file.write("Thanks for your patronage!\n")
        file.write("=" * 30 + "\n")


def read_orders():
    try:
        with open("orders.txt", "r") as file:
            return file.read()

    except FileNotFoundError:
        return ""


def view_orders():
    print("=" * 30)
    print("        ALL ORDERS")
    print("=" * 30)

    orders = read_orders()

    if orders == "":
        print("No orders found.")

    else:
        print(orders)

    print("=" * 30)
