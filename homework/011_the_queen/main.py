import time
import re


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


def get_new_location_and_validity(queen_row, queen_col):
    while True:
        queen_target = input("Enter the queen target destination: ")
        if queen_target == "quit":
            return None, None
        if len(queen_target) != 2:
            print("{} is not a valid board location".format(queen_target))
            continue
        validation_input = re.findall(r"[A-H]\d", queen_target)
        if len(validation_input) == 0:
            print("{} is not a valid board location".format(queen_target))
            continue
        target_row, target_col = target_number(queen_target)
        if target_row != queen_row:
            print("Error: {} is not a valid move.".format(queen_target))
            continue
        if queen_col > target_col:
            print("Error: {} is not a valid direction.".format(queen_target))
            continue
        return target_row, target_col


def move_right(queen_col, target_col, queen_row):
    while queen_col <= target_col:
        print()
        print("The queen is still moving…")
        board(queen_row, queen_col)
        time.sleep(1)
        print()
        queen_col = queen_col + 1
        print()
        print("The queen rests.")
    return queen_col


def main():
    queen_row = 7
    queen_col = 0
    board(queen_row, queen_col)
    print()
    # TODO: handle also move left
    # 1. in get_new_location_and_validity - allow also left
    # 2. in the loop check if moving left or right using queen_col, target_col
    #    if queen_col > target_col --> move_right
    #    if queen_col < target_col --> move_left

    target_row, target_col = get_new_location_and_validity(queen_row, queen_col)
    while target_row is not None:
        queen_col = move_right(queen_col, target_col, queen_row)
        print()
        target_row, target_col = get_new_location_and_validity(queen_row, queen_col)
    print("Okay, bye bye")

main()
