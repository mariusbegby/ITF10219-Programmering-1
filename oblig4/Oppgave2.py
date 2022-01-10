# Oppretter klassen med variabler
class Movie:
    def __init__(self, movie_title, release_year, rating):
        self.movie_title = movie_title
        self.release_year = release_year
        self.rating = rating
    def print_movie(self):
        print(f"{self.movie_title} was released in {self.release_year} and currently has a score of {self.rating}.")


# Lager tre objekter, ett for hver film
inception = Movie("Inception", 2010, 8.8)
the_martian = Movie("The Martian", 2015, 8.0)
joker = Movie("Joker", 2019, 8.4)

print(f"{inception.movie_title} was released in {inception.release_year} and currently has a score of {inception.rating}.")
print(f"{the_martian.movie_title} was released in {the_martian.release_year} and currently has a score of {the_martian.rating}.")
print(f"{joker.movie_title} was released in {joker.release_year} and currently has a score of {joker.rating}.")

inception.print_movie()
the_martian.print_movie()
joker.print_movie()