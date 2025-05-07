"""Jepni pese menyra te ndryshme per te krijuar listen [1,2,3,4,5,6,7,8,9,10]
dhe jepjani ate si vlere ndryshores lst."""

#1. Përdorimi i range() dhe list()
lst = list(range(1, 11))

# 2. Inicializimi direkt
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3. Me list comprehension
lst = [i for i in range(1, 11)]

#4. Me append() brenda një cikli for
lst = []
for i in range(1, 11):
    lst.append(i)

#5. Me extend() dhe një liste tjetër
lst = []
lst.extend(range(1, 11))


