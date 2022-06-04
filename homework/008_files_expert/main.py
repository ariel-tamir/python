import re

file_name = input("Enter file name: ")


def missing_dot():
    line_number = 0
    if file_name.endswith(".txt"):
        with open(file_name, "r") as user_file:
            print("The lines with missing dot at the end are: ")
            for line in user_file:
                line = line.strip()
                line_number = line_number + 1
                if line.endswith("."):
                    pass
                else:
                    print("Line {}: ".format(line_number), line)


def average():
    line_number = 0
    all_averages = 0

    if file_name.endswith(".numbers"):
        with open(file_name, "r") as user_file:
            print("The average for each line is: ")
            for line in user_file:
                line = line.strip()
                line_number = line_number + 1
                numbers_list_strings = re.findall(r"(\d+)", line)
                numbers_list_ints = []
                for string_number in numbers_list_strings:
                    number_int = int(string_number)
                    numbers_list_ints.append(number_int)

                average_line = sum(numbers_list_ints) / len(numbers_list_ints)
                print("Line {}: ".format(line_number), average_line)

                all_averages = all_averages + average_line
                averages_average = all_averages / line_number

            print("The average of all the averages is: {}".format(averages_average))


missing_dot()
average()
