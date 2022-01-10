# Oppgave 5.1
# Oppgave A: lage liste med dictionaries
movies = [
    {
        "name": "Inception",
        "year": 2010,
        "rating": 8.7
    },
    {
        "name": "Inside Out",
        "year": 2015,
        "rating": 8.1
    },
    {
        "name": "Con Air",
        "year": 1997,
        "rating": 6.9
    }
]

# Oppgave B: Opprette funksjon som legger til film i listen. Modifisert fra oppgave C for default rating.
def add_movie(movie_list, name, year, rating=5.0):
    movie_list.append({
        "name": name,
        "year": year,
        "rating": rating
    })

# Oppgave C: Legge til 3 filmer med funksjonen + en film uten rating for å teste default rating
add_movie(movies, "Parasite", 2019, 8.6)
add_movie(movies, "Slumdog Millionaire", 2008, 8.0)
add_movie(movies, "Bohemian Rhapsody", 2018, 7.9)
add_movie(movies, "Black Mirror: Bandersnatch", 2018)

# Printer ut listen med filmer til slutte for å sjekke at alt har blitt lagt til riktig.
print(movies)


# Oppgave 5.2
# Oppgave A: Funksjon for print av liste
def print_movies(movie_list):
    print("")
    for movie in movie_list:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")

print_movies(movies)

# Oppgave B: Gjennomsnittsrating i liste
def average_rating(movie_list):
    rating_sum = 0
    for movie in movie_list:
        rating_sum = rating_sum + movie['rating']
    average_rating = rating_sum / len(movie_list)
    return average_rating

print("")
print(f"Average rating is {average_rating(movies)}.")


# Oppgave C: Funksjon som returnerer liste med filmer fra gitt årstall
def movies_from_year(movie_list, year):
    new_movie_list = []
    for movie in movie_list:
        if movie["year"] >= year:
            new_movie_list.append(movie)
    return new_movie_list

# Bruker funksjonen fra oppgave A til å printe ut liste med filmer fra 2010.
print_movies(movies_from_year(movies, 2010))

# Oppgave 5.3

# Oppgave A: Filmliste til fil
def movie_names_to_file(movie_list, filename):
    file = open(filename, "w")
    movie_titles = ""
    for movie in movie_list:
        movie_titles += f"{movie['name']}\n"
    file.write(movie_titles)
    file.close()

movie_names_to_file(movies, "movie_titles.txt")

# Oppgave B: Lese filmliste fra fil
def read_movie_names_file(filename):
    file = open(filename, "r")
    print(f"\n{file.read()}")

read_movie_names_file("movie_titles.txt")