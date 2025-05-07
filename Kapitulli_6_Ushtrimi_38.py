"""Shkruani nje funksion rekursiv qe gjen pjesetuesin
me te madh te perbashket te dy numrave natyrore """
def pmp(a, b):
    if b == 0:
        return a
    else:
        return pmp(b, a % b)

# Shembull përdorimi
a = int(input("Shkruaj numrin e parë: "))
b = int(input("Shkruaj numrin e dytë: "))

if a < 0 or b < 0:
    print("Të lutem jep vetëm numra natyrorë (pozitivë).")
else:
    print(f"Pjesëtuesi më i madh i përbashkët i {a} dhe {b} është: {pmp(a, b)}")

"""PMP(a, b) është e barabartë me PMP(b, a % b).

Kur b bëhet 0, atëherë PMP është a.

Kjo vazhdon derisa të mos ketë mbetje në pjesëtim.
pmp(48, 18)
→ pmp(18, 48 % 18) = pmp(18, 12)
→ pmp(12, 18 % 12) = pmp(12, 6)
→ pmp(6, 12 % 6) = pmp(6, 0)
→ kthen 6
"""