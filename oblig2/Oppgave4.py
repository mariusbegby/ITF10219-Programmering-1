# Liste over bøker fra sluttresultatet av oppgave 3
tolkien_books = ['Farmer Giles of Ham',
                    'Lord of the Rings: The Fellowship of the Ring',
                    'Lord of the Rings: The Return of the King',
                    'Lord of the Rings: The Two Towers',
                    'The Adventures of Tom Bombadil',
                    'The Hobbit',
                    'The Silmarillion',
                    'Tree and Leaf',
                    'Unfinished Tales']

# Tom liste hvor vi skal legge til LOTR bøkene fra liste i oppgave 3 (den ovenfor)
lotr_bok_liste = []

# Itererer over listen fra oppgave 3, og legger kun til bøkene i lotr_bok_liste dersom navnet inneholder "Lord of the Rings:"
for bok in tolkien_books:
    if "Lord of the Rings:" in bok:
        lotr_bok_liste.append(bok)

# Metode 1: Vanlig for each løkke
for bok in lotr_bok_liste:
    print(bok)

# Metode 2: Det samme, men men bruker indeksen til elementet istedenfor selve elementet
for index in range(len(lotr_bok_liste)):
    print(lotr_bok_liste[index])

# Metode 3: "List Comprehension", en shorthand måte å iterere over lister på?
# Kilde: https://www.w3schools.com/python/python_lists_comprehension.asp
[print(book) for book in lotr_bok_liste]