def iThjeshte(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

for i in range(2, 13):
    print(i, "\t", iThjeshte(i))
