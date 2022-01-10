## Teorioppgave 1

### A: Beskriv med egne ord hva en dictionary er i python og forklar forskjellen på disse og vanlige lister. Trekk frem fordeler og ulemper ved begge.

Et dictionary i Python holder på informasjon i et nøkkel:verdi format. Et dictionary er også på en måte en liste, og kan holde på flere slike nøkkel:verdi par.

### B: Det finnes to måter å hente ut en verdi fra en dictionary. Vis og beskriv forskjellen på disse to.

Har vi et dictionary:
```python
dictionary = {
    "fornavn": "Marius",
    "etternavn": "Begby"
}
```

Så kan vi hente det ut slik:

```python
dictionary["fornavn"]
# eller
dictionary.get("fornavn", "Ingen fornavn") # .get(key, default)
```

Forskjellen er at med .get() funksjonen, kan vi sette en default verdi, dersom det ikke skulle være en verdi som blir hentet ut fra dictionariet.

## Teorioppgave 2

### Funksjoner er ekstremt nyttige i alle former for programmering. Diskuter hvorfor dette er tilfellet. Fokuser på hva fuksjoner gjør og hvordan de kan benyttes, og hvilke effekter bruken av disse har på hvordan en programmerer kan skrive, lese og opprettholde kode.

Funksjoner innholder en kodeblokk som kjører når funksjonen blir kalt, og kan også ta i mot argumenter som skal brukes i denne kodeblokken. Det gjør at vi kan kjøre kode som egentlig gjør det samme, flere ganger, men enkelt med forskjellige variabler. Det gjør koden dynamisk, og vi slipper endre kode flere steder i et dokumenter om vi tar i bruk funksjoner riktig, da trenger vi bare endre koden til funksjonen. Har man lik kode som skal kjøres mer enn to ganger, burde man nok lage en funksjon for det. Koden blir enklere å opprettholde og tilpasse, og det fremmer dynamisk kodeskriving.
