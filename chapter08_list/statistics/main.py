def main():
    number = input("Enter number: ")
    numbers = []
    while number != "done":
        number = int(number)
        numbers.append(number)
        number = input("Enter number: ")
    highest = max(numbers)
    print("the maximum is: {}".format(highest))

    lowest = min(numbers)
    print("the minimum is: {}".format(lowest))

    average = sum(numbers)/len(numbers)
    print("the average is: {}".format(average))

main()