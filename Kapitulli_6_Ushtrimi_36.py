"""Shkruani nje funksion rekursiv
qe gjen shumen e dy numrave natyrore me ane te mbledhjes se perseritur """
def shuma(a, b):
    if b == 0:
        return a
    else:
        return shuma(a + 1, b - 1)

# Marrja e numrave nga përdoruesi
a = int(input("Shkruaj numrin e parë (natyror): "))
b = int(input("Shkruaj numrin e dytë (natyror): "))

# Kontroll nëse numrat janë natyrorë
if a < 0 or b < 0:
    print("Të lutem shkruaj vetëm numra natyrorë (>= 0).")
else:
    rezultati = shuma(a, b)
    print(f"Shuma e {a} dhe {b} është: {rezultati}")



"""Ky funksion përdor rekursion për të shtuar b tek a, por pa përdorur a + b direkt.

Në çdo hap:

a + 1 do të thotë që i shtojmë një njësi tek a.

b - 1 do të thotë që heqim një njësi nga b.

Kur b == 0, do të ndalet dhe do të kthejë rezultatin final që është shuma totale.

Shembull:
Për shuma(4, 3), ndodhin këto hapa:
shuma(4, 3)
→ shuma(5, 2)
→ shuma(6, 1)
→ shuma(7, 0)
→ kthen 7
"""
