def board(x_row, x_col):
    for row in range(4):
        for col in range(4):
            if x_row == row and x_col == col:
                print("X", end="")
            else:
                print("O", end="")
        print()


def main():
    board(2, 3)


main()
