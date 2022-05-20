import array as arr
#Modify
a = arr.array('i',[66, 44, 83, 56, 22, 10])
print(a)
a[0] = 33
print(a)

#Array Count
x = len(a)
print(x)

#Array-merge
a.append(50)
print(a)
a.extend([2, 4, 7, 100])
print(a)

#Array-slicing
a_list = [2, 7, 8, 99, 2000, 111]
a_array = arr.array('i', a_list)
print(a_array[2:6])
print(a_array[:4])
print(a_array[:])
print(a_array[:5])

#Array-loop
#array('i', [33, 44, 83, 56, 22, 10, 50, 2, 4, 7, 100])
for x in a:
    print(x)