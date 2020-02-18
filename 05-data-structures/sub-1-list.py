fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('fruits 1st', fruits)
countApple = fruits.count('apple')
print('countApple:', countApple)
countTangerine = fruits.count('tangerine')
print('countTangerine:', countTangerine)

print('index banana:', fruits.index('banana'))
print('index banana 4:', fruits.index('banana', 4))  # Find next banana starting a position 4
fruits.reverse()
print('after reverse:',fruits)
fruits.append('grape')
print('after append grape:',fruits)
fruits.sort()
print('after sort:', fruits)
fruits.pop()
print('after pop:', fruits)