def eshte_palindrom(num):
    num_str = str(num)
    if len(num_str) <= 1:
        return True
    if num_str[0] != num_str[-1]:
        return False
    return eshte_palindrom(num_str[1:-1])

# Shembull përdorimi:
print(eshte_palindrom(121))  # True
print(eshte_palindrom(123))  # False
