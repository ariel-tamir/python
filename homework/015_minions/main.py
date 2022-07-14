from minion import Minion


def add_from_file():
    file_name = input("Enter file name:")
    with open(file_name, "r") as user_file:
        for line in user_file:
            minion = Minion(line)


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

    print("Okay, bye bye")


main()
