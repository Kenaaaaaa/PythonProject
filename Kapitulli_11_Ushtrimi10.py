"""Shkruani një program që ruan 100 numrat e parë të plotë në një skedar teksti të quajtur numrat.txt.
Çdo numër të shfaqet në një rresht më vete."""

def sumfile(emri_skedarit):
    with open(emri_skedarit, "w") as skedar:
        for i in range(1, 101):  # nga 1 deri në 100
            skedar.write(str(i) + "\n")

# Thirrja e funksionit
sumfile("numrat.txt")
