import random


def new_player(balance):
    print()
    name = input("Enter your name: ")
    cash = random.randint(50, 100)
    print("Welcome {}, we randomized for your entry amount of {}$.".format(name, cash))
    balance[name] = cash


def balances(balance):
    print("The balances are: ")
    for name, cash in balance.items():
        print("{} {}$".format(name, cash))


def play(balance):
    print()
    while True:
        user_name = input("Enter your name: ")
        if user_name in balance:
            break
        else:
            print("Error!")
    user_bet = input("How much money do you want to bet on? ")
    dice_result = random.randint(1, 6)
    print("Rolling the dice…… The dice shows {}.".format(dice_result))
    if 1 <= dice_result <= 3:
        print("The bet is lost")
    elif 4 <= dice_result <= 5:
        print("No profit")
    elif dice_result == 6:
        print("You won!!")


def print_menu():
    print("1. Add new player")
    print("2. Show balances")
    print("3. Play")
    print("4. Quit ")


def main():
    balance = {}
    print_menu()
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
        print_menu()
        user_selection = input("Enter your selection: ")
        user_selection = int(user_selection)


main()
