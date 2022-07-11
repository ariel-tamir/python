import re
from actor import Actor


class Actors:
    def __init__(self):
        self.actors_list = []

    def list_actors_by_age(self):
        age_range = input("Enter actors age range: ")
        validation_input = re.findall(r"^\d+-\d+$", age_range)
        while True:
            if len(validation_input) == 0:
                print("{} is not a valid input".format(age_range))
                age_range = input("Enter actors age range: ")
                validation_input = re.findall(r"^\d+-\d+$", age_range)
            else:
                break
        parts = age_range.split(sep="-")
        from_age = parts[0]
        from_age = int(from_age)
        to_age = parts[1]
        to_age = int(to_age)
        print("Matching actors are: ")
        for actor in self.actors_list:
            if actor.is_in_age_range(from_age, to_age):
                print(actor.name, "({} movies)".format(len(actor.movies) - 1))

    def add_actor(self):
        actor_name = input("Enter the actor’s name: ")
        actor_birth_year = input("Enter the actor’s birth year: ")
        validation_input = re.findall(r"^\d+$", actor_birth_year)
        while True:
            if len(validation_input) == 0:
                print("{} is not a valid input".format(actor_birth_year))
                actor_birth_year = input("Enter the actor’s birth year: ")
                validation_input = re.findall(r"^\d+$", actor_birth_year)
            else:
                break
        actor_movies = []
        movie_count = 0
        actor_movie = input("Enter the actor’s movies, or click Enter to complete: ")
        actor_movies.append(actor_movie)
        while actor_movie != '':
            actor_movie = input("Enter the actor’s movies, or click Enter to complete: ")
            actor_movies.append(actor_movie)
            movie_count = movie_count + 1
        actor = Actor(actor_name, actor_birth_year, actor_movies)
        self.actors_list.append(actor)
        print("OK, actor {} added, and {} movies specified.".format(actor_name, movie_count))

    def delete_actor(self):
        actor_name = input("Enter actor name: ")
        self.delete_actor_by_name(actor_name)

    def delete_actor_by_name(self, actor_name):
        for index, actor in enumerate(self.actors_list):
            if actor.name == actor_name:
                self.actors_list.pop(index)
                print("OK, the actor {} was deleted.".format(actor_name))
                return
        print("actor not found")

    def delete_movie(self):
        actors_to_delete = []
        actor_movie = input("Enter movie name: ")
        for actor in self.actors_list:
            if actor_movie in actor.movies:
                actors_to_delete.append(actor.name)
        for delete in actors_to_delete:
            self.delete_actor_by_name(delete)
