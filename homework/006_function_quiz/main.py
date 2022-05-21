def main():
    number = input("Enter number: ")
    numbers = []

    while number != "done":

        try:
            number = int(number)
            is_number = True
        except:
            print("Invalid input")
            is_number = False

        if is_number:
            numbers.append(number)
        number = input("Enter number: ")

    total = sum(numbers)
    count = len(numbers)
    average = sum(numbers) / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    print("Results are: total: {}, count: {}, average: {}, maximum: {}, minimum: {} ".format(total, count, average,
                                                                                             highest, lowest))


main()
