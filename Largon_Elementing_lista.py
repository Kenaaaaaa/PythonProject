def largo_te_fundit(lista, vlera):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == vlera:
            del lista[i]
            break
    return lista

# Shembull përdorimi:
lista = [5, 7, 3, 7, 2, 7]
print(largo_te_fundit(lista, 7))  # [5, 7, 3, 7, 2]
