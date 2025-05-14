"""Numëroni numrin e shfaqjeve të karakterit të parë në stringun e dhënë."""
stringu = input("Shkruani një string: ")

if stringu != "":
    karakteri_i_pare = stringu[0]
    numerues = 0
    for karakter in stringu:
        if karakter == karakteri_i_pare:
            numerues += 1
    print("Karakteri i parë është:", karakteri_i_pare)
    print("Ai shfaqet", numerues, "herë në string.")
else:
    print("Stringu është bosh.")
