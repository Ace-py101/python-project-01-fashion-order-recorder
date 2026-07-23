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
    read_orders
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

    print("Edit feature will be improved after refactor.")


def delete_order():

    print("=" * 30)
    print("       DELETE ORDER")
    print("=" * 30)

    print("Delete feature will be improved after refactor.")
