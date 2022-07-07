class Actor:
    def __init__(self, name, birth_year, movies):
        self.name = name
        self.birth_year = birth_year
        self.movies = movies

    def is_in_age_range(self, from_age, to_age):
        self.birth_year = 2022 - self.birth_year
        if from_age <= self.birth_year <= to_age:
            return True
        else:
            return False

    def is_in_movie(self, movie_name):
        if movie_name in self.movies:
            return True
        else:
            return False
