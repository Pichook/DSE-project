customer_name = input("Enter name:")
units = int(input("Enter your unit:"))

if units > 700:
    price = 4000.00
elif units > 500:
    price = 3000.00
elif units > 400:
    price = 2000.00
else:
    price = 1500.00

print("Customer name:", customer_name)
print("Total unit consumption:", units)
print("Price per unit:", price, "Riels")
print("Total payable amount:", units*price, "Riels")










