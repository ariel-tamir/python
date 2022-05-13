def main():
    number = input("Enter number: ")
    number = int(number)
    for row in range(number):
        for col in range(number):
            print("*", end="")
        print()


main()
