n = int(input("Shkruani një numër të plotë pozitiv: "))

if n < 1:
    pass  # Nuk printon asgjë nëse numri është më i vogël se 1
else:
    for i in range(n):
        print('*' * n)







"""Shkruani nje program python qe pranon nje vlere te vetme te plote te dhene nga perdoruesi.
Nese vlera eshte me e vogel se 1, programi nuk printong asgje.
Nese perdoruesi fut nje numer te pltoe pozitiv, n, programi printon nje kuti nxn te vizatuar me *.
Neser perodruesi fut 1, per shembull programi printon *
Nese perodruesi fut 2, ai printon
**
**
Nje hyrje prej tre jep
***
***
***
Nese perdoruesi fut 7, ai printon
*******
*******
*******
*******
*******
*******
*******
dmth nje kuti 7x7 simbole
"""