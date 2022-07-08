from class_actor import Actor
import re


def list_actors_by_age(actors_list):
    age_range = input("Enter actors age range: ")
    print("Matching actors are: ")
    for actor in actors_list:
        actor.is_in_age_range(from_age, to_age)


def add_actor(actors_list):
    actor_name = input("Enter the actor’s name: ")
    actor_birth_year = input("Enter the actor’s birth year: ")
    validation_input = re.findall(r"\d+", actor_birth_year)
    while True:
        if len(validation_input) == 0:
            print("{} is not a valid input".format(actor_birth_year))
            actor_birth_year = input("Enter the actor’s birth year: ")
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
    actor_delete = input("Enter actor name: ")
    actors_list.remove(actor_delete)
    print("OK, the actor {} was deleted.".format(actor_delete))


def delete_movie():
    movie_delete = input("Enter movie name: ")


def print_menu():
    print()
    print("1. List actors by age")
    print("2. Add actor")
    print("3. Delete actor")
    print("4. Delete movie")
    print("5. Quit")
    print()


def main():
    print_menu()
    actors_list = []
    user_selection = input("Enter your selection: ")
    user_selection = int(user_selection)
    while user_selection != 5:
        if user_selection == 1:
            list_actors_by_age(actors_list)
        elif user_selection == 2:
            add_actor(actors_list)
        elif user_selection == 3:
            delete_actor()
        elif user_selection == 4:
            delete_movie()
        print_menu()
        user_selection = input("Enter your selection: ")
        user_selection = int(user_selection)
    print("OK, have a good one!")


main()
