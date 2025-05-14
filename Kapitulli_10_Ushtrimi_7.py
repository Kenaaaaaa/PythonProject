"""Fusni karakterin ◆ në mes të çdo fjale në një fjali."""
fjali = input("Shkruani një fjali: ")
fjalet = fjali.split()  # ndan fjalinë në fjalë
rezultati = " ◆ ".join(fjalet)
print("Rezultati:", rezultati)