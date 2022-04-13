def main():
    number = input("enter number: ")
    number = int(number)
    for row in range(number):
        for col in range(row + 1):
            print(col + 1, end="")
        print()


main()
