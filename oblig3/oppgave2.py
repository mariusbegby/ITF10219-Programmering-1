from random import randrange

# Definerer funksjonen
def tilfeldig_tall():
    tall = randrange(0, 100) # Genererer tilfeldig tall mellom 0 og 100
    print("\n**********")
    print(f"*** {str(tall).zfill(2)} ***") # Legger til leading zeroes for fint output når tall < 10
    print("**********")

# Kaller funksjonen 3 ganger, kan også f.eks. bruke for loop for å kalle den flere ganger.
tilfeldig_tall()
tilfeldig_tall()
tilfeldig_tall()