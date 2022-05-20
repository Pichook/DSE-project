age = int(input("Enter age: "))
criminal_records = input("Criminal record, true or false: ")

if age>=18:
    age = True
else:
    age = False
if criminal_records=='True':
    criminal_records = False
elif criminal_records=='False':
    criminal_records = True

if age and criminal_records:
    print("You are eligible for the job!")
elif age or criminal_records:
    print("May need to review your records.")
elif not age and not criminal_records:
    print("Not eligible.")