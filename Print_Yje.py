#Sa yje shfaq fragmenti i kodit te meposhtem print?

a=0
while a<100:
    b=0
    while b<55:
        print('*',end='')
        b+=1
    print()
    a+=1

"""Ky kod do të shfaqë 5,500 yje (të shkruara si '*') të organizuara në 100 rreshta, ku çdo rresht përmban 55 yje.
Shpjegim i hollësishëm:
Loop-i i jashtëm (while a < 100):
Përsëritet 100 herë (nga a=0 deri në a=99).
Çdo herë që ekzekutohet, inicializon b=0 dhe fillon loop-in e brendshëm.
Loop-i i brendshëm (while b < 55):
Përsëritet 55 herë për çdo përsëritje të jashtme (nga b=0 deri në b=54).
Në çdo përsëritje të brendshme, printohet një yll ('*') pa kalim në rresht të ri (end='').
Pasi të përfundojë loop-i i brendshëm, print() shton një rresht të ri.
Numri total i yjeve:
100 rreshta × 55 yje/rresht = 5,500 yje."""