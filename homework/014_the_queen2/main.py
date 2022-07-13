from board import Board


def main():
    board = Board()
    board.board()
    print()
    target_row, target_col = board.get_new_location_and_validity()
    while target_row is not None:
        if board.queen_col < target_col:
            board.move_right(target_col)
            print()
            target_row, target_col = board.get_new_location_and_validity()
        elif board.queen_col > target_col:
            board.move_left(target_col)
            print()
            target_row, target_col = board.get_new_location_and_validity()
        elif board.queen_row > target_row:
            board.move_up(target_row)
            print()
            target_row, target_col = board.get_new_location_and_validity()
        elif board.queen_row < target_row:
            board.move_down(target_row)
            print()
            target_row, target_col = board.get_new_location_and_validity()
    print("Okay, bye bye")


main()
