t = 12345, 54321, 'hello!'
print('t[0]', t[0])
print('t', t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print('u', u)
# Tuples are immutable:
t[0] = 88888
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print('v', v)