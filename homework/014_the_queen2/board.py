import re
import time


class Board:
    def __init__(self):
        self.queen_row = 7
        self.queen_col = 0

    def board(self):
        for row in range(8):
            print(8 - row, " ", end="")
            for col in range(8):
                if self.queen_row == row and self.queen_col == col:
                    print("♕ ", end="")
                else:
                    print("🨇 ", end="")
            print()
        print("  A B C D E F G H")

    def get_col(self, letter):
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

    def get_row(self, number):
        number = int(number)
        number = 8 - number
        return number

    def target_number(self, queen_target):
        letter = queen_target[0]
        number = queen_target[1]
        col = self.get_col(letter)
        row = self.get_row(number)
        return row, col

    def get_new_location_and_validity(self):
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
            target_row, target_col = self.target_number(queen_target)
            if self.queen_row != target_row and self.queen_col != target_col:
                print("{} is not a valid board location".format(queen_target))
                continue
            return target_row, target_col

    def move_right(self, target_col):
        while self.queen_col < target_col:
            print()
            print("The queen is still moving…")
            self.board()
            time.sleep(1)
            print()
            self.queen_col = self.queen_col + 1
        self.board()
        print()
        print("The queen rests.")

    def move_left(self, target_col):
        while self.queen_col > target_col:
            print()
            print("The queen is still moving…")
            self.board()
            time.sleep(1)
            print()
            self.queen_col = self.queen_col - 1
        self.board()
        print()
        print("The queen rests.")

    def move_up(self, target_row):
        while self.queen_row > target_row:
            print()
            print("The queen is still moving…")
            self.board()
            time.sleep(1)
            print()
            self.queen_row = self.queen_row - 1
        self.board()
        print()
        print("The queen rests.")

    def move_down(self, target_row):
        while self.queen_row < target_row:
            print()
            print("The queen is still moving…")
            self.board()
            time.sleep(1)
            print()
            self.queen_row = self.queen_row + 1
        self.board()
        print()
        print("The queen rests.")

