number = int(input("Enter number here: "))
i = 0
num_str = ""

while number>0:
    print(number)
    i = int(number %10)
    number = number // 10
    num_str+=str(i)
