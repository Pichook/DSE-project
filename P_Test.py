student_id= input("Student ID: ")
student_name = input("Student name: ")
mark1 = 60
mark2 = 75
mark3 = 90
res = mark1 + mark2 +mark3
res_avg = res/3

if student_name == 'John':
    print("Result: ", res)
    print("Average: ", res_avg)
else:
    print("Who are you?")
