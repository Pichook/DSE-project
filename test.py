number = int(input("Enter number here: "))
i = 0
num_str = ""

while number > 0:
    i = number %10
    number = number//10

print(number)