# Tolkning av oppgaven: Fra og med 9 til 101 (står ikke til og med 101, så 101 er ikke med, kun til og med 100)
print("Printer ut oddetall med for loop:")
for tall in range(9, 101): # For hvert tall i området 9 til 101
    if tall % 2 == 1: # Sjekker om tall er oddetall, modulo 2 vil gi 1 i rest hvis tallet er oddetall (fordi det ikke går opp med 2), skal vi finne partall sjekker vi om rest er 0.
        print(tall) # Skriver ut tallet, bare om det er oddetall.

print("\nPrinter ut oddetall med while loop:")
teller = 9 # Med en while loop trenger vi også en teller, som vi kan inkrementere for å til slutt stoppe loopen.
while(teller < 101): # Så lenge telleren ikke er lik eller over 101, så fortsetter den og kjører koden på nytt.
    if teller % 2 == 1:
        print(teller)
    teller = teller + 1 # Her øker vi telleren med en, slik at loopen kan til slutt bli ferdig. Dette gjøres uansett om det er partall eller oddetall.