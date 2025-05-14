a=5
b=7
print('a=',a,'b=',b)
a,b=b,a
print('a=',a, 'b =',b)


x=(2,6,4,2,9)
y=[2,6,4,2,9]
print(x[1])

#Tuple nuk ndryshon
print(x[1:5])

print(dir(tuple))
print(x.index(6))
print(dir(int))
kofini={'molle','portokalle','pjeshke','banane'}
kof={'molle','portokalle','pjeshke','banane','portokalle','banane'}
print(len(kofini))
kofini.add('arra')
print(len(kofini))
kofini.add('lajthi')
kofini.pop()

kofini2=['limon', 'qershi' , 'hider','pjeshke']
print(kofini.difference((kofini2)))  # jep diferenen qe nuk kane prerje
print(kofini.intersection(kofini2))
print(kofini.issuperset(kofini2))
ab=['molle','portokalle']
print(kofini.issuperset(ab))
emer='Brikena'
print(emer)
adresa="Pallati me shigjeta"
print(adresa)
poezi='''Kush din mue me m'tregue
por kjo qyqja zog i true
po vajton n'hijen e pemes
 .......'''
print(poezi)
eplote=emer+" "+adresa
print(eplote)
print(emer*4+" ")
print(emer+" "+str(5))
print(emer<adresa)
print(emer>adresa)
print(emer[0]<adresa[0])
print(poezi[0:15])
#kur vendosim index e trete, i treti esht ehapi
print(poezi[0:15:2])
print(poezi[5:0:-1])
print(poezi[1::2])

print(dir(str))
print(emer.index('r'))
print(emer.isalpha())
print(emer.isalnum())
datelindje=["18", "10","1973"]
print(":".join(datelindje))
print(poezi.split('i')) #simboli qe i ndan, behet delete
print(emer.capitalize())
print(emer.upper())
print(emer.lower())
print(poezi.swapcase())
print("Tung {}".format(emer))
print("Tung ",emer)
print("Tung "+emer)
print('{0} {2} {1}'.format('kena','agalliu','tirana'))
print(f"Emri im eshte {emer}")
print(emer.center(30))#emri vendoset ne qender te hapesires me 30
print(emer.ljust(30))
print(emer.rjust(30))
print(dir(int))
print(dir(float))
print(a.to_bytes())
print(b.to_bytes())
print(emer.__getitem__(0))
emer[0]
print(emer.__sizeof__())
print(len(emer))

try:
    f = open("skedarin.txt", 'r')
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("Skedari nuk u gjet.")

