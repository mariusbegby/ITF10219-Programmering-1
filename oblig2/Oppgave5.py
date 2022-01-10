# Importerer randrange() funksjonen til senere bruk for å generere tilfeldige tall.
from random import randrange

# Setter innledende variabler og spør bruker om antall spillere som skal spille.
print(f"=== DART ===")
totale_poeng = []
antall_piler_hver = 3
antall_spillere = int(input("Hvor mange spillere? Skriv antall: "))
print(f"{antall_spillere} spillere valgt. Dere har {antall_piler_hver} piler hver.")

for spiller in range(antall_spillere): # For hver spiller
    spiller_poeng = 0 # Setter poengene til den enkelte spilleren til 0 før kast
    print(f"\nDet er spiller nummer {spiller + 1} som skal kaste nå.")

    kast_pil = input(f"Trykk en tast og ENTER for å kaste pilene dine.") # Spilleren må bekrefte kast med å skrive noe i konsoll og trykke enter.
    if kast_pil:
        for kast in range(antall_piler_hver): # For hver pil som blir kastet, generer en tilfeldig score og legg til i total score for spilleren.
            score = randrange(0, 60)
            spiller_poeng = spiller_poeng + score
            print(f"Du kastet en pil og fikk {score} poeng.")
    print(f"Du fikk totalt {spiller_poeng} poeng.") 
    totale_poeng.append(spiller_poeng) # Til slutt, legg til poengene for den enkelte spilleren til en liste over alle spillerene sine totale poeng.

print("\n=== TOTALE POENG ===")
for index in range(len(totale_poeng)): # Skriver ut de totale poengene for hver spiller etter at alle har kastet.
    print(f"Spiller nummer {index + 1}: {totale_poeng[index]} poeng")

vinner = totale_poeng.index(max(totale_poeng)) # Beregner hvilken spiller som vant ved å hente ut index til høyeste score
print(f"\nSpiller nummer {vinner + 1} vant med {totale_poeng[vinner]} poeng, gratulerer!")

# Løsning for del A, uten flere spillere
#print(f"Du har {antall_piler} piler igjen.")
#while antall_piler > 0:
#    kast_pil = input("Trykk en hvilken som helst tast og ENTER for å kaste en pil.")
#    if kast_pil:
#        antall_piler = antall_piler - 1
#        antall_kastet += antall_kastet
#        score = randrange(0, 60)
#        totale_poeng = totale_poeng + score
#        print(f"Du kastet en pil og fikk {score} poeng, du har {antall_piler} piler igjen.")
#        if antall_piler == 0:
#            print(f"Din totale score ble: {totale_poeng} poeng")