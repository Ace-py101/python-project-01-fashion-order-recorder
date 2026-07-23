import json


FILE_NAME = "orders.json"


def load_orders():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_order(order):

    orders = load_orders()

    orders.append(order)

    with open(FILE_NAME, "w") as file:
        json.dump(
            orders,
            file,
            indent=4
        )


def view_orders():

    print("=" * 30)
    print("        ALL ORDERS")
    print("=" * 30)

    orders = load_orders()

    if not orders:
        print("No orders found.")

    else:
        for order in orders:

            print("-" * 30)

            print("Customer Name :", order["customer_name"])
            print("Phone Number  :", order["phone_number"])
            print("Garment Type  :", order["garment_type"])
            print("Quantity      :", order["quantity"])
            print("Delivery Date :", order["delivery_date"])
            print("Price         : ₦", order["price"])
            print("Deposit       : ₦", order["deposit"])
            print("Balance       : ₦", order["balance"])

    print("=" * 30)

def save_all_orders(orders):

    with open(FILE_NAME, "w") as file:
        json.dump(
            orders,
            file,
            indent=4
        )
