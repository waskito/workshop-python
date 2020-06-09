a = [-1, 1, 66.25, 333, 333, 1234.5]
print('a', a)
del a[0]
print('a after del a[0]', a)
del a[2:4]
print('a after del a[2:4]', a)
del a[:]
print('a after del a[:]', a)