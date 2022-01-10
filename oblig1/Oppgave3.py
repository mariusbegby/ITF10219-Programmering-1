# Her må brukerinput gjøres om til typen float (nummer med desimaler), hvis ikke blir tallene lagret som string.
tall1 = float(input("Velg tall nummer 1: "))
tall2 = float(input("Velg tall nummer 2: "))

# Her utføres de aritmetiske operasjonene før svarene printes ut til konsollen.
# Vi printer ut tekst i tillegg til "tallsvaret", slik at brukeren enkelt kan se hva som ble utført på hver linje.
print("\nHer er dine kalkulasjoner:")
print(f"{tall1} * {tall2} (gange) = {tall1 * tall2}") # gange
print(f"{tall1} / {tall2} (dele) = {tall1 / tall2}") # dele
print(f"{tall1} + {tall2} (pluss) = {tall1 + tall2}") # pluss
print(f"{tall1} - {tall2} (minus) = {tall1 - tall2}") # minus
print(f"{tall1} % {tall2} (modulo) = {tall1 % tall2}") # modulo / rest
print(f"{tall1} ** {tall2} (opphøye) = {tall1 ** tall2}") # opphøye tall1 i tall 2
print(f"{tall1} // {tall2} (dele m/ nedrunding) = {tall1 // tall2}") # dele, men gjøres om til int(), altså nedrunding