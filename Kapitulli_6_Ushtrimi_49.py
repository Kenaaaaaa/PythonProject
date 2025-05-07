"""Shkruani nje funksion rekursiv, perseritje,
qe kthen numrin e perseritjeve te nje vlere te dhene nje nje vektor/liste """

def numer_perseritje(lista, vlera):
    if not lista:
        return 0
    elif lista[0] == vlera:
        return 1 + numer_perseritje(lista[1:], vlera)
    else:
        return numer_perseritje(lista[1:], vlera)


# Leximi i listës nga përdoruesi
teksti = input("Shkruaj elementet e listës të ndara me hapësira: ")
lista = list(map(int, teksti.split()))

# Leximi i vlerës që duam të kërkojmë
vlera = int(input("Shkruaj vlerën që do të kërkosh: "))

# Thirrja e funksionit
rezultati = numer_perseritje(lista, vlera)

# Shfaqja e rezultatit
print(f"Vlera {vlera} është përsëritur {rezultati} herë në listë.")

#if not lista: kontrollon nëse lista është bosh (rasti bazë).
#Nëse elementi i parë është i barabartë me vlerën, kthen 1 + pjesa tjetër.

