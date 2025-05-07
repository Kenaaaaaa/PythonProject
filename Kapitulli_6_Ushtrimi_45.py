"""Shkruani nje funksion rekursiv qe gjen dhe kthen shumen e elementeve
te nje liste int. Gjithashtu, shkruani nje program per te testuar funksionin tuaj."""

def shuma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + shuma_lista(lista[1:])

# Leximi i elementeve nga përdoruesi
teksti = input("Shkruaj elementet e listës të ndara me hapësira: ")

# Konvertimi i tekstit në listë integer-ash
elementet = list(map(int, teksti.split()))

# Thirrja e funksionit dhe shfaqja e rezultatit
print("Lista:", elementet)
print("Shuma e elementeve të listës është:", shuma_lista(elementet))

#Shkruaj elementet e listës të ndara me hapësira: 3 7 1 4
#Lista: [3, 7, 1, 4]
#Shuma e elementeve të listës është: 15

