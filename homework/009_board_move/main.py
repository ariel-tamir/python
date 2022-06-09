def board(x_row, x_col):
    for row in range(4):
        for col in range(4):
            if x_row == row and x_col == col:
                print("X", end="")
            else:
                print("O", end="")
        print()


def main():
    x_row = 0
    x_col = 0
    board(x_row, x_col)
    move_x = input("Enter your move: ")
    while move_x != "quit":

        if move_x == "up":
            x_row = x_row - 1
            if x_row < 0:
                print("Error: unable to move up.")
            else:
                board(x_row, x_col)
        elif move_x == "down":
            x_row = x_row + 1
            if x_row > 3:
                print("Error: unable to move down.")
            else:
                board(x_row, x_col)
        elif move_x == "right":
            x_col = x_col + 1
            if x_col > 3:
                print("Error: unable to move right.")
            else:
                board(x_row, x_col)
        elif move_x == "left":
            x_col = x_col - 1
            if x_col < 0:
                print("Error: unable to move left.")
            else:
                board(x_row, x_col)
        else:
            print("Error")
            quit()

        move_x = input("Enter your move: ")


main()
