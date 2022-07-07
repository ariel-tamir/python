from class_actor import Actor


def list_actors_by_age(actor_name):
    actor_name.is_in_age_range()


def add_actor(actors_list):
    actor_name = input("Enter the actor’s name: ")
    actor_birth_year = input("Enter the actor’s birth year: ")
    actor_movies = []
    actor_movie = input("Enter the actor’s movies, or click Enter to complete: ")
    actor_movies.append(actor_movie)
    while actor_movie != '':
        actor_movie = input("Enter the actor’s movies, or click Enter to complete: ")
        actor_movies.append(actor_movie)
    actor = Actor(actor_name, actor_birth_year, actor_movies)
    actors_list.append(actor)


def delete_actor():


def delete_movie():


def main():
    print("1. List actors by age")
    print("2. Add actor")
    print("3. Delete actor")
    print("4. Delete movie")
    print("5. Quit")
    print()
    actors_list = []
    user_selection = input("Enter your selection: ")
    user_selection = int(user_selection)
    while user_selection != 5:
        if user_selection == 1:
            list_actors_by_age()
        elif user_selection == 2:
            add_actor()
        elif user_selection == 3:
            delete_actor()
        elif user_selection == 4:
            delete_movie()


main()
