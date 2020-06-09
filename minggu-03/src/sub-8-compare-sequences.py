comp1 = (1, 2, 3)              < (1, 2, 4)
comp2 = [1, 2, 3]              < [1, 2, 4]
comp3 = 'ABC' < 'C' < 'Pascal' < 'Python'
comp4 = (1, 2, 3, 4)           < (1, 2, 4)
comp5 = (1, 2)                 < (1, 2, -1)
comp6 = (1, 2, 3)             == (1.0, 2.0, 3.0)
comp7 = (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

print(comp1,comp2,comp3,comp4,comp5,comp6,comp7)