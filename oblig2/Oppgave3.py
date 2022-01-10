# Liste over noen bøker skrevet av Tolkien
tolkien_books = ["The Hobbit",
                    "Farmer Giles of Ham",
                    "The Fellowship of the Ring",
                    "The Two Towers",
                    "The Return of the King",
                    "The Adventures of Tom Bombadil",
                    "Tree and Leaf"]

# A: Skrive ut de to først og to siste bøkene i listen
print(f"To første bøker i listen: '{tolkien_books[0]}' og '{tolkien_books[1]}'")
print(f"To siste bøker i listen: '{tolkien_books[-2]}' og '{tolkien_books[-1]}'")

# B: Legg til to bøker utgitt etter hans død
tolkien_books.extend(["The Silmarillion", "Unfinished Tales"])

# C: Legge til Lord of the Rings prefix på de tre lotr bøkene
lotr_prefix = "Lord of the Rings:"
tolkien_books[tolkien_books.index("The Fellowship of the Ring")] = f"{lotr_prefix} The Fellowship of the Ring"
tolkien_books[tolkien_books.index("The Two Towers")] = f"{lotr_prefix} The Two Towers"
tolkien_books[tolkien_books.index("The Return of the King")] = f"{lotr_prefix} The Return of the King"

# D: Sorterer listen og så skriver den ut
tolkien_books.sort()
print("\nSortert liste over bøkene:")
print(tolkien_books)