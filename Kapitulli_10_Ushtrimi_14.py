"""Zëvendësoni zanoren me një karakter të caktuar."""
teksti = input("Shkruani një tekst: ")
zanore = "aeiouAEIOU"
rezultati = ""

for shkronje in teksti:
    if shkronje in zanore:
        rezultati += "*"
    else:
        rezultati += shkronje

print("Rezultati:", rezultati)
