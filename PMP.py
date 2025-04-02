

a=int(input("Jep nr1"))
b=int(input("Jep nr2"))
mbetja=a%b
while mbetja>0:
    a=b
    b=mbetja
    mbetja=a%b
print(b)

