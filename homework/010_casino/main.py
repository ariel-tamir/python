import random


def new_player():
    print()
    name = input("Enter your name: ")
    cash = random.randint(50, 100)
    print("Welcome {}, we randomized for your entry amount of {}$.".format(name, cash))


def main():
    print("1. Add new player")
    print("2. Show balances")
    print("3. Play")
    print("4. Quit ")
    user_selection = input("Enter your selection: ")
    user_selection = int(user_selection)
    if user_selection == 1:
        new_player()


main()
