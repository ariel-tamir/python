import random


def new_player(balance):
    print()
    name = input("Enter your name: ")
    cash = random.randint(50, 100)
    print("Welcome {}, we randomized for your entry amount of {}$.".format(name, cash))
    balance[name] = cash
    print(balance)


def balances(balance):
    pass

def play(balance):
    pass


def main():
    balance = {}
    print("1. Add new player")
    print("2. Show balances")
    print("3. Play")
    print("4. Quit ")
    user_selection = input("Enter your selection: ")
    user_selection = int(user_selection)
    while user_selection != 4:
        if user_selection == 1:
            new_player(balance)
        elif user_selection == 2:
            balances(balance)
        elif user_selection == 3:
            play(balance)

        print()
        user_selection = input("Enter your selection: ")


main()
