from minion import Minion


def print_menu():
    print()
    print("1. Add minions from file")
    print("2. Save minions to file|")
    print("3. List minions")
    print("4. Assign job")
    print("5. Report job complete")
    print("6. Quit")
    print()


def main():
    print_menu()
    minion = Minion()
    user_selection = input("Enter your selection: ")
    while user_selection != 6:
        if user_selection == 1:
            minion.constructor()


main()
