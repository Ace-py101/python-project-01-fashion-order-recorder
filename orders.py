from validation import (
    get_customer_name,
    get_phone_number,
    get_garment_type,
    get_quantity,
    get_delivery_date,
    get_price,
    get_deposit
)

from receipt import display_receipt

from storage import (
    save_order,
    view_orders,
    load_orders,
    save_all_orders,
    generate_order_id
)

def create_order():

    customer_name = get_customer_name()
    phone_number = get_phone_number()
    garment_type = get_garment_type()
    quantity = get_quantity()
    delivery_date = get_delivery_date()
    price = get_price()
    deposit = get_deposit(price)

    balance = price - deposit

    order_id = generate_order_id()

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

    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "phone_number": phone_number,
        "garment_type": garment_type,
        "quantity": quantity,
        "delivery_date": delivery_date,
        "price": price,
        "deposit": deposit,
        "balance": balance
    }

    save_order(order)

    print("Order saved successfully.")

def search_order():

    print("=" * 30)
    print("      SEARCH ORDER")
    print("=" * 30)

    while True:
        try:
            search_id = int(input("Enter Order ID: "))
            break
        except ValueError:
            print("Please enter numbers only.")

    orders = load_orders()

    found = False

    for order in orders:

        if order["order_id"] == search_id:

            found = True

            print("\nOrder Found")
            print("=" * 30)
            print("Order ID      :", order["order_id"])
            print("Customer Name :", order["customer_name"])
            print("Phone Number  :", order["phone_number"])
            print("Garment Type  :", order["garment_type"])
            print("Quantity      :", order["quantity"])
            print("Delivery Date :", order["delivery_date"])
            print("Price         : ₦", order["price"])
            print("Deposit       : ₦", order["deposit"])
            print("Balance       : ₦", order["balance"])
            print("=" * 30)

            break

    if not found:
        print("Order not found.")

def edit_order():

    print("=" * 30)
    print("       EDIT ORDER")
    print("=" * 30)

    while True:
        try:
            search_id = int(input("Enter Order ID: "))
            break
        except ValueError:
            print("Please enter numbers only.")

    orders = load_orders()

    found = False

    for order in orders:

        if order["order_id"] == search_id:

            found = True

            print("\nCurrent Order")
            print("=" * 30)
            print("Order ID      :", order["order_id"])
            print("Customer Name :", order["customer_name"])
            print("Phone Number  :", order["phone_number"])
            print("Garment Type  :", order["garment_type"])
            print("Quantity      :", order["quantity"])
            print("Delivery Date :", order["delivery_date"])
            print("Price         : ₦", order["price"])
            print("Deposit       : ₦", order["deposit"])
            print("Balance       : ₦", order["balance"])
            print("=" * 30)

            print("\nEnter new details:")

            order["garment_type"] = get_garment_type()
            order["quantity"] = get_quantity()
            order["delivery_date"] = get_delivery_date()
            order["price"] = get_price()
            order["deposit"] = get_deposit(order["price"])
            order["balance"] = order["price"] - order["deposit"]

            save_all_orders(orders)

            print("Order updated successfully.")

            break

    if not found:
        print("Order not found.")


def delete_order():

    print("=" * 30)
    print("      DELETE ORDER")
    print("=" * 30)

    while True:
        try:
            search_id = int(input("Enter Order ID: "))
            break
        except ValueError:
            print("Please enter numbers only.")

    orders = load_orders()

    updated_orders = []
    found = False

    for order in orders:

        if order["order_id"] == search_id:

            found = True

            print("\nOrder Found")
            print("=" * 30)
            print("Order ID      :", order["order_id"])
            print("Customer Name :", order["customer_name"])
            print("Phone Number  :", order["phone_number"])
            print("Garment Type  :", order["garment_type"])
            print("Quantity      :", order["quantity"])
            print("Price         : ₦", order["price"])
            print("=" * 30)

            confirm = input(
                "Delete this order? (Y/N): "
            ).strip().lower()

            if confirm == "y":
                print("Order deleted successfully.")
                continue

        updated_orders.append(order)

    if not found:
        print("Order not found.")
        return

    save_all_orders(updated_orders)
