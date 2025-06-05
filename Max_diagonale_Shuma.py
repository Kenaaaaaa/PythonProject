def maksimum_dhe_shuma(matrix):
    n = len(matrix)
    max_diag = matrix[0][0]
    shuma = 0
    for i in range(n):
        shuma += matrix[i][i]
        if matrix[i][i] > max_diag:
            max_diag = matrix[i][i]
    return max_diag, shuma

# Shembull përdorimi për matricën nga figura:
matrix = [
    [8, 8, 10, 7, 6, 7, 7, 7],
    [8, 10, 7, 6, 7, 7, 7, 0],
    [10, 7, 6, 7, 7, 0, 0, 0],
    [7, 6, 7, 7, 0, 0, 0, 0],
    [6, 7, 7, 0, 0, 0, 0, 0],
    [7, 7, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0]
]

maks, shuma = maksimum_dhe_shuma(matrix)
print("Maksimumi në diagonale:", maks)
print("Shuma:", shuma)
