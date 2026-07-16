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
while True:
  try:
    quantity = int(input("Enter Quantity: "))

    if quantity >= 1:
      break

    print("Quantity cannot be less than 1")  

  except ValueError:
    print("Invalid input")
    
print("Quantity:   ",quantity)
delivery_date = input("Enter Delivery Date:")
print("Delivery date   :",delivery_date)
while True:
   try:
     price = int(input("Enter Price:"))

     if price > 0:
       break
       
     print("Price must be greater than zero.")
     
   except ValueError:
     print("Please enter numbers only.")
     
print("Price   :N",price)
while True:
   try:
     deposit = int(input("Enter deposit:"))

     if deposit > 0 and deposit <= price:
       break

     print("Deposit must be greater than zero and must not exceed the price.")

   except ValueError:
    print ("Please enter numbers only")
    
print("Deposit   :N",deposit)
balance = price - deposit
print("Balance   :N",balance)
print("==============================")
print("Thanks for your patronage!")
print("==============================")
