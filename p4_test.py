import array as arr

a = arr.array('i', [23, 44, 45, 21, 8, 33, 55])
max = a[0]
for i in range(0, len(a)):
    if (a[i] > max):
        max = a[i]

print("Maximum number: ", str(max))