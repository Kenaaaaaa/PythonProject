"""Ushtrimi 7:
“Duke pasur parasysh fjalorin e mëposhtëm:

Tregoni se çfarë do të printojë secili nga fragmentet e kodit të mëposhtëm:”

Opsionet janë:

(a) print(d)

(b) for x in d: print(x)

(c) for x in d.keys(): print(x)

(d) for x in d.values(): print(x)"""

#a) Zgjidhja
d = {3:0, 5:1, 10:1, 8:2, 15:4}
print(d)
#Do printojë të gjithë fjalorin:
#{3: 0, 5: 1, 10: 1, 8: 2, 15: 4}

# b) Zgjidhja
for x in d: print(x)
"""Ky kod do te  printoje:
3
5
10
8
15
"""
# c) Zgjidhja
for x in d.keys(): print(x)
"""Ky kod do te printoje 
3
5
10
8
15
"""
# d) Zgjidhja
for x in d.values(): print(x)
"""Ky kod do te printoje 
0
1
1
2
4


"""