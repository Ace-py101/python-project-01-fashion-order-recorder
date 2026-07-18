from datetime import datetime
# ==========================
# Fashion House Order Recorder
# Project 1
# Author: Sobowale Oluwatobi
# ==========================

# Collect customer information

print("==============================")
print("      CLIENT RECEIPT")
print("==============================")
while True:
  customer_name = input("Enter Customer name: ").strip()

  if customer_name == "":
    print("Customer name cannot be empty.")  
    continue

  if not  customer_name.replace(" ","").isalpha():
    print("Customer name can only contain letters and spaces")
    continue

  if len(customer_name.replace(" ","")) < 3:
    print("Customer name must contain at least 3 letters.")
    continue

  customer_name = " ".join(customer_name.split()).title()

  break  
        
print("Customer name   :",customer_name)
while True:
  phone_number = input("Enter phone number: ").strip()

  if phone_number == "":
    print("Phone number cannot be empty")
    continue

  if not phone_number.replace(" ","").isdigit():
    print("Phone number can only contain numebers")
    continue

  if len(phone_number)!= 11:
    print("Phone number cannot be less than 11 digits")
    continue

  if not phone_number.startswith("0"):
    print("Phone number must start with zero")
    continue

  break

print("Phone number   :",phone_number)
while True:
  garment_type = input ("Enter garment type: ").strip()

  if garment_type == "":
    print("Garment type cannot be empty")
    continue

  if not garment_type.replace(" ","").isalpha():
    print("Garment type can only contain letters and spaces")
    continue

  if len(garment_type.replace(" ","")) < 3:
    print("Garment must contain at least 3 letters")
    continue

  garment_type = " ".join(garment_type.split()).title()

  break
    
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
while True:
  delivery_date = input("Enter deliver date (DD/MM/YYYY): ").strip()

  if delivery_date == "":
    print("Delivery date cannot be empty")
    continue

  try:
    datetime.strptime(delivery_date, "%d/%m/%Y")
    break

  except ValueError:
    print("Please enter the date in DD/MM/YYYY formart")
      
print("Delivery date   :",delivery_date)
while True:
   try:
     price = int(input("Enter Price: "))

     if price > 0:
       break
       
     print("Price must be greater than zero.")
     
   except ValueError:
     print("Please enter numbers only.")
     
print("Price   :N",price)
while True:
   try:
     deposit = int(input("Enter deposit: "))

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
