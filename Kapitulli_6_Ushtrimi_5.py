"""
Cila nga vlerat e meposhtme mund te prodhohet nga thirrja e funksionit random.randrange(0,100)
(rrethoni gjithcka qe zbatohet) 4.5 34 -1 100 0 99?
"""
import random

print(random.randrange(0,100))

"""Funksioni random.randrange(0, 100) do të gjenerojë një numër të rastësishëm të plotë nga 0 deri në 99, duke përfshirë 0, por pa përfshirë 100.

Pra, ai mund të printojë çdo numër si:
0, 1, 2, 3, ..., 97, 98, 99


4.5  → Jo, sepse është numër dhjetor (jo i plotë)
34 → Po, sepse është numër i plotë brenda intervalit 0–99
-1  → Jo, sepse është më i vogël se 0
100  → Jo, sepse random.randrange(0, 100) nuk e përfshin 100
0  → Po, sepse është pika e fillimit e intervalit
99  → Po, sepse është maksimumi që mund të gjenerohet (100 është i përjashtuar)

✅ Pra, mund të printojë: 0, 34, 99
❌ Nuk mund të printojë: 4.5, -1, 100

"""