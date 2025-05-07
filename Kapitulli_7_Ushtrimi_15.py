"""Plotesoni funksionin e meposhtem qe shumon te gjitha vlerat pozitive ne nje liste me numra te plote. Per shembull, nese lista a permban elementet 3; -3 ; 5 ; 2; -1; dhe 2, thirrja sum_pozitive (a) do te vleresohej ne 12, pasi 3+5+2+2=12.
Funksioni kthen zero nese lista eshte bosh. def sum_positive(a): #Shkruani kodin ...."""

def sum_positive(a):
    if not a:
        return 0
    elif a[0] > 0:
        return a[0] + sum_positive(a[1:])
    else:
        return sum_positive(a[1:])

# Leximi i listës nga përdoruesi
teksti = input("Shkruaj numrat e listës të ndarë me hapësira: ")
lista = list(map(int, teksti.split()))

# Llogaritja dhe shfaqja e rezultatit
print("Shuma e vlerave pozitive në listë është:", sum_positive(lista))

"""Shkruaj numrat e listës të ndarë me hapësira: 3 -3 5 2 -1 2
Shuma e vlerave pozitive në listë është: 12
"""