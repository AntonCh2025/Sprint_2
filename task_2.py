class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f"Комедии: '{self.movies}'")


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        print(f"Драмы: '{self.movies}'")


comedy = Comedy()
comedy.add_movie('Большой куш')
drama = Drama()
drama.add_movie('Оружейный барон')
