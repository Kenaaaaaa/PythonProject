
def pmp(a,b):
    mbetja=a%b
    while mbetja>0:
        a=b
        b=mbetja
        mbetja=a%b
    return b
nr1 = int(input("Jep nr1"))
nr2 = int(input("Jep nr2"))
print("PMP =",pmp(nr1,nr2))



