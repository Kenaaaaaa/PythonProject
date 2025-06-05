def eshte_simetrike(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Shembull përdorimi:
matrix = [
    [8, 8, 10],
    [8, 10, 7],
    [10, 7, 6]
]

print(eshte_simetrike(matrix))  # False në këtë rast
