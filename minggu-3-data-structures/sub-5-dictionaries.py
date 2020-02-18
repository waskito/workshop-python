tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print('tel', tel)
tel['jack']
del tel['sape']
tel['irv'] = 4127
print('tel', tel)
print('list(tel)', list(tel))
print('sorted(tel)', sorted(tel))
print("'guido' in tel", 'guido' in tel)
print("'jack' not in tel", 'jack' not in tel)