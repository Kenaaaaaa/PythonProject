"""A eshte i rregullt programi i meposhtem meqe ndryshorja x perdoret ne dy vende te ndryshme
(proc dhe main)? Perse? """

def proc(x):
    return 2*x*x  # kjo x është parametri i funksionit proc

def main():
    x=10   # kjo x është një ndryshore *lokale* brenda main
    print(proc(x))  # kjo x i dërgohet si argument funksionit proc
main()     # Këtu thirret funksioni main

"""
    return 2*x*x  # kjo x është parametri i funksionit proc
    x = 10        # kjo x është një ndryshore *lokale* brenda main
    print(proc(x))  # kjo x i dërgohet si argument funksionit proc
    main()  # Këtu thirret funksioni main
    Në Python, çdo funksion ka hapësirën e vet të ndryshoreve që quhet scope.
    x brenda main() është lokale për atë funksion dhe nuk ka lidhje direkte me x në proc(x).
    Kur thërret proc(x), po i dërgon vlerën 10 si argument, dhe proc punon me këtë vlerë të dhënë.
    Pra, përdorimi i të njëjtit emër x në funksione të ndryshme nuk shkakton konflikt, 
    sepse janë lokale dhe të ndara nga njëra-tjetra.

"""
