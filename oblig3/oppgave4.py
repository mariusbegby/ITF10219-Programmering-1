# Definerer funksjonen som beregner omkrets
def beregn_omkrets(lengde, bredde):
    omkrets = 2 * lengde + 2 * bredde
    return omkrets

# Kan printe ut resultatet direkte slik
print(beregn_omkrets(4, 5))

# Eller ta i bruk variabler
lengde = 8
bredde = 17
omkrets = beregn_omkrets(lengde, bredde) # omkrets variabelen vil få verdien som beregn_omkrets() returnerer.
print(f"Omkretsen til et rektangel med {lengde} som lengde og {bredde} som bredde er {omkrets}.")