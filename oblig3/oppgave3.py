# Definerer funksjonen, tar en liste som argument
def print_list(liste):
    for element in liste: # Printer ut hvert element med bruk av for loop
        print(element)

# Lager en liste med 3 dyr
favoritt_dyr = ["Reptiler", "Fisk", "Blekksprut"]

# Kaller funksjonen med listen som parameter
print_list(favoritt_dyr)