import re

from class_actor import Actor


def list_actors_by_age(actors_list):
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
    for actor in actors_list:
        if actor.is_in_age_range(from_age, to_age):
            print(actor.name, "({} movies)".format(len(actor.movies) - 1))


def add_actor(actors_list):
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
    actors_list.append(actor)
    print("OK, actor {} added, and {} movies specified.".format(actor_name, movie_count))


def delete_actor(actors_list):
    actor_name = input("Enter actor name: ")
    delete_actor_by_name(actors_list, actor_name)


def delete_actor_by_name(actors_list, actor_name):
    for index, actor in enumerate(actors_list):
        if actor.name == actor_name:
            actors_list.pop(index)
            print("OK, the actor {} was deleted.".format(actor_name))
            return
    print("actor not found")


def delete_movie(actors_list):
    actors_to_delete = []
    actor_movie = input("Enter movie name: ")
    for actor in actors_list:
        if actor_movie in actor.movies:
            actors_to_delete.append(actor.name)
    for delete in actors_to_delete:
        delete_actor_by_name(actors_list, delete)


def print_menu():
    print()
    print("1. List actors by age")
    print("2. Add actor")
    print("3. Delete actor")
    print("4. Delete movie")
    print("5. Quit")
    print()


def valid_input_user_selection():
    user_selection = input("Enter your selection: ")
    validation_input = re.findall(r"^[1-5]$", user_selection)
    while True:
        if len(validation_input) != 1:
            print("{} is not a valid input".format(user_selection))
            user_selection = input("Enter your selection: ")
            validation_input = re.findall(r"^[1-5]$", user_selection)
        else:
            user_selection = int(user_selection)
            return user_selection


def main():
    print_menu()
    actors_list = []
    user_selection = valid_input_user_selection()
    while user_selection != 5:
        if user_selection == 1:
            list_actors_by_age(actors_list)
        elif user_selection == 2:
            add_actor(actors_list)
        elif user_selection == 3:
            delete_actor(actors_list)
        elif user_selection == 4:
            delete_movie(actors_list)
        print_menu()
        user_selection = valid_input_user_selection()
    print("OK, have a good one!")


main()
