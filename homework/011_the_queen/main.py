def board(x_row, x_col):
    for row in range(8):
        print(8 - row, " ", end="")
        for col in range(8):
            if x_row == row and x_col == col:
                print("♕ ", end="")
            else:
                print("🨇 ", end="")
        print()
    print("  A B C D E F G H")


def get_col(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2
    elif letter == "D":
        return 3
    elif letter == "E":
        return 4
    elif letter == "F":
        return 5
    elif letter == "G":
        return 6
    elif letter == "H":
        return 7


def get_row(number):
    number = int(number)
    number = 8 - number
    return number


def target_number(queen_target):
    letter = queen_target[0]
    number = queen_target[1]
    col = get_col(letter)
    row = get_row(number)
    return row, col


def main():
    queen_row = 7
    queen_col = 0
    board(queen_row, queen_col)
    print()
    queen_target = input("Enter the queen target destination: ")
    while queen_target != "quit":
        target_row, target_col = target_number(queen_target)
        if target_row != queen_row:
            print("Error: {} is not a valid move.".format(queen_target))
            queen_target = input("Enter the queen target destination: ")
        else:
            while queen_col <= target_col:
                board(queen_row, queen_col)
                print()
                queen_col = queen_col + 1
            print()
            queen_target = input("Enter the queen target destination: ")
    print("Okay, bye bye")


main()

