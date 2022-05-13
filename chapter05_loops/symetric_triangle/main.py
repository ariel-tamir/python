def print_row(row, number):
    for i in range(number - row + 1):
        print(" ", end="")
    for col in range(row + 1):
        print(col + 1, end="")
    for col in reversed(range(row)):
        print(col + 1, end="")
    print()


def main():
    number = input("enter number: ")
    number = int(number)
    for row in range(number):
        print_row(row, number)


main()
