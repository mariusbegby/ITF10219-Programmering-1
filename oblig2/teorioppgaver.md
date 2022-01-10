# Teorioppgaver

## Teorioppgave 1 - if-test

### Forklar hva en if-test er med egne ord. Beskriv ogs\ sammenhengen mellom if, elif og else.

En if-test eller "if statement" er en funksjon som tar i mot en uttalelse, som enten er sann eller usann (`True` eller `False`). Dersom denne uttalelsen er sann, vil koden i kodeblokken innenfor if-testen kjøre. Dermed kan if-tester brukes til å kjøre kode bare dersom noe annet skjer, eller hvis en variabel har en viss verdi eller ikke. Eksempel:

```python
number1 = 7
number2 = 35
if (number1 + number2 == 42):
    print("Nummer 1 + nummer 2 er lik 42")
# output: Nummer 1 + nummer 2 er lik 42

number1 = 5
number2 = 7
if (number1 + number2 == 42):
    print("Nummer 1 + nummer 2 er lik 42")
# output:
```

## Teorioppgave 2 - for-løkke

### Forklar hva en for-løkke er og gi noen eksempler på tilfeller man kan ønske å benytte dem.

En for-løkke eller for-loop er en "løkke" som kjører om og om igjen, så lenge noe gjenstår. Som regel er det en liste over elementer, eller en rekke med tall som skal itereres. Det er spesielt brukbart om du har en liste med elementer, og du skal gjøre noe med hvert av elementene, eller sjekke/lete etter noe for hvert av elementene. Eksempel:

```python
handleliste = ["Brød", "Melk", "Agurk", "Grandiosa"]
for vare in handleliste:
    print(vare)
# output:
# Brød
# Melk
# Agurk
# Grandiosa
```

Noen ganger ønsker man indeksen til elementene, og ikke selve innholdet til elementene, man kan da lage en for loop slik:

```python
handleliste = ["Brød", "Melk", "Agurk", "Grandiosa"]
for index in range(len(handleliste)):
    print(index)
# output:
# 0
# 1
# 2
# 3
```

## Teorioppgave 3 - liste

### Forklar hva list er i Python og hva den kan brukes til.

Lister eller "Arrays" i Python er noe som inneholder på flere verdier samtidig. Vi har både vanlig liste og tuple. Forskjellen er at tuple ikke kan modifiseres på noen måte etter å ha blitt opprettet, dette kan være nyttig dersom du har et sett med data som du vet ikke skal endre seg. Ellers, så er det vanlig å bruke liste/array. Disse kan inneholde mange verdier, og med flere forskjellige datatyper. Som regel inneholder en liste "like" type elementer, slik at det som er i listen gir mening for seg selv. Eksempel lister:

```python
handleliste = ["Brød", "Melk", "Agurk", "Grandiosa"]
favoritt_tall = [1.1618, "√2", "π", 7]
```

Verdiene fra en liste kan hentes ut ved å spesifisere hvilken indeks i listen den har:

```python
favoritt_tall = [1.1618, "√2", "π", 7]
print(favoritt_tall[1]) # output: √2
print(favoritt_tall[3]) # output: 7
```
