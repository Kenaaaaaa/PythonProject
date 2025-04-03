"""Shkruani nje program Python qe kerkon pese vlera te pòlota nga perdoruesi.
nese futen disa here printo "ka duplikime" nese jo printo" vetem 1 here"
"""

#krijojme nje liste boshe
vlerat=[]
for i in range(5):
    vlera = int(input(f"Shkruaj vlerën e plotë nr. {i+1}: "))
    vlerat.append(vlera)

if len(vlerat)!=len(set(vlerat)):
    print("ka duplikime")
else:
     print("Vetem nje here")
