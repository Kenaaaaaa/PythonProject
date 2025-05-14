"""Konsideroni kortezhin tpl te percaktuar
 si tpl=7,10, -3, 18,6,10 Jepni nje urdherese
  te caktimi qe perdor shpaketimin e kortezhit,
  per te percaktuar x ne elementin e pare dhe y
  ne elementin e fundit
"""
tpl = (7, 10, -3, 18, 6, 10)

x, *z, y = tpl   # ku z përmban elementët e tjerë: [10, -3, 18, 6]


print("x =", x)
print("z =", z)
print("y =", y)

