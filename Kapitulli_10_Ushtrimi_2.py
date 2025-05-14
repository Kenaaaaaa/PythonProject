"""hkruani një program për të numëruar sasinë e karaktereve në string
(Mos përdorni metodën e paracaktuar len)"""

stringu = input("Shkruani një string: ")
numerues = 0
for karakter in stringu:
    numerues += 1

print("Numri i karaktereve:", numerues)
