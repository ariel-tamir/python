def print_list(numbers):
    first = True
    print("The sorted list is: ", end="")
    for number in numbers:
        if first:
            first = False
            print(number, end="")
        else:
            print(",{}".format(number), end="")
    print()


def print_second(numbers):
    first = True
    print("The every second list is: ", end=" ")
    for index in range(len(numbers)):
        if index % 2 == 1:
            if first:
                first = False
                print(numbers[index], end="")
            else:
                print(",{}".format(numbers[index]), end="")


def main():
    number = input("Enter number: ")
    numbers = []
    while number != "done":
        number = int(number)
        numbers.append(number)
        number = input("Enter number: ")

    numbers.sort()
    print_list(numbers)
    print_second(numbers)


main()
