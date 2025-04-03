"""Shkruani nje program Python qe kerkon pese vlera te pòlota nga perdoruesi. Me pas
printon vlere aksimale dhe minimale te tyre. Nese perdoruesi fut vlerat 3,2,5,0 dhe 1 programi do te
tregoje se 5 eshte max dhe 0 eshte min. Programi duhet te trajgoje barazimin ,psh nese perdoruesi fut
2,4,2,3 dhe 3 pgrogrami duhet te raportoje 2 si minimum dhe 4 si max"""

#deklarojme nje liste me emrin vlerat
vlerat=[]

for i in range(5):
    vlera=(int)(input("Fut pese numer"))
    vlerat.append(vlera)

print(f"Maksimumi per vlerat e futura eshte {max(vlerat)} dhe minimumi per vlerat e futura eshte {min(vlerat)}")

