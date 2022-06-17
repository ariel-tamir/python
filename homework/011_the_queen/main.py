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


board(0, 0)
