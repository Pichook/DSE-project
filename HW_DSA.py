#Start:
import array as arr

#Accessing array
a = arr.array('i', [1, 2, 45, 66, 7, 99, 10])
print("First element:", a[0])
print("Last element:", a[-1])

#Insertion
a.append(73)
print(a)

#Deletion
del a[4]
print(a)

a.pop(1)
print(a)



