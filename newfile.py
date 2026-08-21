customer_name=str(input("Enter Customer Name: "))
contact_number=str(input("Enter Contact Number: "))
address=str(input("Enter Address: "))
product_1=str(input("Enter Product 1 Name: "))
price_1 = float(input("Enter Price: "))
quantity_1 = int(input("Enter Quantity: "))
product_2=str(input("Enter Product 2 Name: "))
price_2 = float(input("Enter Price: "))
quantity_2 = int(input("Enter Quantity: "))
product_3=str(input("Enter Product 3 Name: "))
price_3= float(input("Enter Price: "))
quantity_3= int(input("Enter Quantity: "))

amount_1 = price_1 * quantity_1
amount_2 = price_2 * quantity_2
amount_3 = price_3 * quantity_3

sum = amount_1 + amount_2 + amount_3

discount= sum * (10/100)

total = sum - discount

print("Store Recipt")
print("==========================")
print(f"Customer Name : {customer_name}")
print(f"Contact Number : {contact_number}")
print(f"Address : {address}")
print(f"{'Product':<12} {'Price':<8} {'Qty':<6} {'Amount':<8}")
print("-" * 36)
print(f"{product_1:<12} {price_1:<8.2f} {quantity_1:<6} {amount_1:<8.2f}")
print(f"{product_2:<12} {price_2:<8.2f} {quantity_2:<6} {amount_2:<8.2f}")
print(f"{product_3:<12} {price_3:<8.2f} {quantity_3:<6} {amount_3:<8.2f}")
print("============================")

print("---------------------------------------------")
print("Subtotal", sum)
print("Discount (10%)", discount)
print("----------------------------------------------")

print("Total", total)
print("=========================")