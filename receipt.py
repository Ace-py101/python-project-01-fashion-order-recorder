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
