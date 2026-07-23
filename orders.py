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
    load_orders
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
    print("       SEARCH ORDER")
    print("=" * 30)

    search_name = input("Enter customer name: ")

    orders = read_orders()

    if search_name.lower() in orders.lower():
        print("Order found!")
        print("=" * 30)
        print(orders)

    else:
        print("No order found for this customer.")

    print("=" * 30)


def edit_order():

    print("=" * 30)
    print("        EDIT ORDER")
    print("=" * 30)

    search_name = input("Enter customer name: ").strip()

    orders = read_orders()

    order_list = orders.split("==============================\nORDER START\n")

    updated_orders = []
    found = False

    for order in order_list:

        if search_name.lower() in order.lower():

            found = True

            print("\nExisting Order:")
            print(order)

            print("\nEnter new details:")

            new_garment = get_garment_type()
            new_quantity = get_quantity()
            new_price = get_price()
            new_deposit = get_deposit(new_price)

            balance = new_price - new_deposit

            updated_order = f"""
ORDER START
==============================
Customer Name : {search_name.title()}
Garment Type  : {new_garment}
Quantity      : {new_quantity}
Price         : ₦{new_price}
Deposit       : ₦{new_deposit}
Balance       : ₦{balance}
==============================
ORDER END
Thanks for your patronage!
==============================
"""

            updated_orders.append(updated_order)

        else:
            updated_orders.append(order)


    if found:

        with open("orders.txt", "w") as file:
            file.write(
                "==============================\nORDER START\n"
                + "\n".join(updated_orders)
            )

        print("Order updated successfully.")

    else:
        print("Order not found.")


def delete_order():

    print("=" * 30)
    print("       DELETE ORDER")
    print("=" * 30)

    customer_name = input("Enter customer name: ").strip()

    orders = read_orders()

    order_list = orders.split("==============================\nORDER START\n")

    remaining_orders = []
    found = False

    for order in order_list:

        if customer_name.lower() in order.lower():

            found = True

            print("\nOrder Found:")
            print(order)

            confirm = input(
                "Delete this order? (Y/N): "
            ).strip().lower()

            if confirm == "y":
                print("Order deleted successfully.")
                continue

            else:
                remaining_orders.append(order)

        else:
            remaining_orders.append(order)


    if not found:
        print("Order not found.")
        return


    with open("orders.txt", "w") as file:
        file.write(
            "==============================\nORDER START\n"
            + "\n".join(remaining_orders)
        )
