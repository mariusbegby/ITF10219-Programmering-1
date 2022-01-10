# I starten av programmet lager vi en tom pakkeliste, og setter program_open til True
# Brukeren kan avslutte programmet senere ved å bruke QUIT kommandoen og da settes program_open til False
program_open = True
pakkeliste = []
# Liste over kommadoene som brukeren kan skrive inn.
liste_over_kommandoer = ["HELP - Vis denne siden",
                            "PRINT - Print ut pakkeliste",
                            "ADD - Legg til noe i pakkelisten",
                            "DELETE - Slett noe fra pakkelisten",
                            "CHANGE - Endre noe i pakkelisten",
                            "QUIT - Print ut pakkelisten og avslutt programmet"]

# Så lenge brukeren ikke skriver inn QUIT, vil programmet kjøre i en loop og brukeren kan utføre flere kommandoer etter hverandre.
while program_open:
    # Gjør om alle kommandoer til UPPERCASE, slik at input ikke er case sensitive.
    kommando_input = input("\nHva vil du gjøre? Skriv inn kommando. For hjelp, skriv HELP: ").upper()
    if kommando_input == "HELP": # HELP printer ut listen over kommandoer igjen, slik at brukeren kan sjekke dette når som helst.
        for kommando in liste_over_kommandoer:
            print(kommando)
    elif kommando_input == "PRINT": # PRINT skriver ut alle elementene i pakkelisten
        if len(pakkeliste) == 0: # Hvis pakkelisten er tom, så skal den ikke skrive ut elementene i den tomme listen.
            print("\nPakkelisten din er tom. Legg til noe ved å bruke ADD kommandoen.")
        else:
            print(f"\nHer er pakkelisten din: ")
            for index in range(len(pakkeliste)):
                print(f"{index + 1}. {pakkeliste[index]}")
    elif kommando_input == "QUIT": # QUIT vil avslutte programmet, men også skrive ut listen før den avslutter.
        print("\nPrinter ut pakkelisten før avslutning:")
        if len(pakkeliste) > 0:
            for index in range(len(pakkeliste)):
                print(f"{index + 1}. {pakkeliste[index]}")
        print("\nAvslutter pakkeliste programmet.")
        program_open = False
    elif kommando_input == "ADD": # ADD vil la brukeren legge til noe i pakkelisten
        item_to_add = input("\nHva vil du legge til i pakkelisten? ")
        pakkeliste.append(item_to_add)
        print(f"Du har lagt til {item_to_add} i pakkelisten.")
    elif kommando_input == "DELETE": # DELETE vil la brukeren slette noe i pakkelisten
        item_to_delete = int(input("\nHva vil du fjerne fra pakkelisten? Skriv inn nummer: "))
        pakkeliste.pop(item_to_delete - 1)
        print(f"Du har slettet element {item_to_delete} fra pakkelisten.")
    elif kommando_input == "CHANGE": # CHANGE vil la brukeren endre på en ting i pakkelisten
        item_to_change = int(input("\nHvilket element vil du endre på? Skriv inn nummer: "))
        item_change = input("Hva vil du endre til? ")
        print(f"\nDu har endret {pakkeliste[item_to_change - 1]} til {item_change}.")
        pakkeliste[item_to_change - 1] = item_change
    else:
        print("Det er ikke en kommando, prøv igjen.")
