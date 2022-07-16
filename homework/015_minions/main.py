from minions import Minions


def print_menu():
    print()
    print("1. Add minions from file")
    print("2. Save minions to file")
    print("3. List minions")
    print("4. Assign job")
    print("5. Report job complete")
    print("6. Quit")
    print()


def main():
    print_menu()
    minions = Minions()
    user_selection = input("Enter your selection: ")
    while user_selection != 6:
        if user_selection == 1:
            minions.add_from_file()
        elif user_selection == 2:
            minions.save_minions_to_file()
        elif user_selection == 3:
            minions.list_minions()
        elif user_selection == 4:
            minions.assign_job()
        elif user_selection == 5:
            minions.report_job_complete()
        print_menu()
    print("Okay, bye bye")


main()
