import re

from actor import Actor
from actors import Actors


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
    actors = Actors()
    print_menu()
    user_selection = valid_input_user_selection()
    while user_selection != 5:
        if user_selection == 1:
            actors.list_actors_by_age()
        elif user_selection == 2:
            actors.add_actor()
        elif user_selection == 3:
            actors.delete_actor()
        elif user_selection == 4:
            actors.delete_movie()
        print_menu()
        user_selection = valid_input_user_selection()
    print("OK, have a good one!")


main()
