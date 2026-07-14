# ==========================
# Fashion House Order Recorder
# Project 1
# Author: Sobowale Oluwatobi
# ==========================

# Collect customer information

print("==============================")
print("      CLIENT RECEIPT")
print("==============================")
customer_name = input("Enter Customer name:")
print("Customer name   :",customer_name)
phone_number = input("Enter Phone number:")
print("Phone number   :",phone_number)
garment_type = input("Enter Garment type:")
print("Garment type   :",garment_type)
quantity = int(input("Enter Quantity:"))
print("Quantity:   ",quantity)
delivery_date = input("Enter Delivery Date:")
print("Delivery date   :",delivery_date)
price = int(input("Enter Price: "))
while price <= 0:
    print("Price must be greater than zero.")
    price = int(input("Enter Price:"))
print("Price   :N",price)
deposit = int(input("Enter Deposit:"))
while deposit <= 0 or deposit > price:
    print("Deposit must be greater than zero, and cannot be more than price.")
    deposit = int(input("Enter Deposit:"))
print("Deposit   :N",deposit)
balance = price - deposit
print("Balance   :N",balance)
print("==============================")
print("Thanks for your patronage!")
print("==============================")
