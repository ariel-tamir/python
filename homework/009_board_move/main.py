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
        move_x = input("Enter your move: ")
        if move_x == "up":
            x_row = x_row - 1
            board(x_row, x_col)
        elif move_x == "down":
            x_row = x_row + 1
            board(x_row, x_col)
        elif move_x == "right":
            x_col = x_col + 1
            board(x_row, x_col)
        elif move_x == "left":
            x_col = x_col - 1
            board(x_row, x_col)
        else:
            print("Error")
            quit()


main()
