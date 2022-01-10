# Antall spiste småkaker per person.
person1, person2, person3, person4, person5 = 5, 9, 2.5, 21, 0

# Lager en liste (array) med personene
liste_antall_småkaker = [person1, person2, person3, person4, person5]

# Summerer antall småkaker fra listen, og deler på antall i listen, så gjør om til integer og printer ut.
print(f"Gjennomsnitt antall spiste småkaker: {int(sum(liste_antall_småkaker)/len(liste_antall_småkaker))}")