import re


def main():
    count_numbers = 0
    all_lines = 0
    file_name = input("Enter file name: ")
    with open(file_name, "r") as user_file:
        for line in user_file:
            numbers_in_line = re.findall(r"\d+", line)
            if len(numbers_in_line) >= 1:
                print(line)
                count_numbers = count_numbers + 1
            all_lines = all_lines + 1
            no_number_line = all_lines - count_numbers
        print("The file has {} lines, {} of them with numbers, and {} without numbers.".format(all_lines, count_numbers,
                                                                                               no_number_line))


main()
