from homework.012_actors.class_actor import Actor

def list_actors_by_age():


def add_actor():


def delete_actor():


def delete_movie():


def main():
    print("1. List actors by age")
    print("2. Add actor")
    print("3. Delete actor")
    print("4. Delete movie")
    print("5. Quit")
    print()
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
