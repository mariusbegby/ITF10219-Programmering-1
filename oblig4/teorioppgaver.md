## Teorioppgave 1

### Forklar hva en exception er, og i hvilke tilfeller det er relevant og håndtere dette.

En exception i Python kommer av at noe uventet har skjedd. Som regel en feil i koden eller feil fra brukerinput. Disse feilene som har oppstått uventet kan være mye forskjellig. F.eks. at vi forsøker å gjøre om bokstaver til tall, det går ikke. Da vil Python komme med en exception, representert som et objekt. Vi kan behandle en enkelt type exception eller alle typer exception. Dette gjøres som regel med try-except statements:

```python
try:
    int("Dette er en streng med tekst")
except:
    print("En feil har oppstått.")

# koden i try: vil forsøke å bli kjørt, bare dersom en feil oppstår blir koden i except: kjørt.
```

## Teorioppgave 2

### Forklar med egne ord hva en klasse er, gi gjerne et enkelt eksempel.

En klasse i Python fungerer som en mal til å opprette andre objekter. Da spesifiserer man hvilke egenskaper / nøkler og data disse objektene skal ha, og man kan enkelt opprette nye objekter i likt format ved å benytte klassen. Klasser kan også ha funksjoner for å gjøre noe med dataene til objektet, som er veldig nyttig når du har like objekter du vil gjøre like ting med, f.eks.: Endre navn på noe i et objekt. Eksempel på en klasse:

```python
Class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def addCourse(self, courseName):
        self.courses.append(courseName)


marius = Student("Marius Begby")
marius.addCourse("Programmering 1")
```

## Teorioppgave 3

### Forklar med egne ord hva et objekt er, og hva dens relasjon til klasser er. 

Et objekt er en instanse av en klasse og en datatype i Python som kan holde på flere forskjellige typer data. Når vi bruker "malen" til en klasse for å opprette en ny instans av klassen, blir et objekt laget. Objekter kan holde på mange typer data. Vi kan enkelt endre og oppdatere verdiene til et objekt.
