# Bruker samme dyr som blir gitt som eksempel i oppgaven
animal = {
    "species" : "HoneyBadger",
    "name" : "Nils",
    "sex" : "Male"
}

# Skriver ut navnet på dyret
print(f"Navn på dyret: {animal['name']}")

# Kjønnsoperasjon + alder
animal["sex"] = "Female"
animal["age"] = 22

# Skriver ut informasjonen om dyret
print(f"Alderen til dyret {animal['name']} er {animal['age']} år og dyret er en {animal['sex']} {animal['species']}.")