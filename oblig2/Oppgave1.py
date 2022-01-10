# Samler inn input fra brukeren og gjør om til heltall.
tall_fra_bruker = int(input("Hva er meningen med livet? "))

if tall_fra_bruker == 42: # Bare hvis tallet er nøyaktig 42
    print("Det stemmer, meningen med livet er 42!")
elif tall_fra_bruker > 30 and tall_fra_bruker < 50: # Hvis ikke, men hvis tall er over 30 og under 50.
    print("Nærme, men feil.")
else: # Hvis ikke, skriv ut "FEIL!"
    print("FEIL!")