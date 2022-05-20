num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
num3 = int(input("Enter number:"))

if num1<num2:
    if num2<num3:
        print("Number 3 is the greatest number.")
    else:
        print("Number 2 is the greatest.")
elif num1>num2:
    if num1>num3:
        print("Number 1 is the greatest.")
    else:
        print("Number 3 is the greatest.")