import array as arr

number = arr.array('i', [1, 2, 2, 3, 4])
number.append(5)
print(number)
number.extend([7,8,9])
print(number)

number_list = [1,2,3,4,5,6,88]
number_array = arr.array('i', number_list)
print(number_array[0:5])