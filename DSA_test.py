import array as arr

a_list = [1, 2, 66, 53, 99, 80, 99, 102]
a_array = arr.array('i', a_list)
print(a_array[2:6])
print(a_array[:6])
print(a_array[1:])
print(a_array[:])