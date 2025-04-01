#Cfare printon fragmenti i kodit qe vijon

a=0
while a>100:
    print(a)
    a+=1
print()

"""Ky kod nuk do të printojë asgjë përveç një rreshti bosh në fund (print()).

Shpjegimi:
Kushti i while (a > 100):
a fillon me vlerën 0.
0 > 100 nuk plotesohet kushti, kështu që loop-i while nuk ekzekutohet fare.
Pra, print(a) dhe a += 1 nuk thirren asnjëherë.
print() në fund: Ky thjesht shton një rresht bosh në dalje, por nuk shfaq asnjë vlerë të a."""