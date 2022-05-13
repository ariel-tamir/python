import os


def create_file():
    name = input("Enter player name: ")
    age = input("Enter player age: ")
    file_name = "data\\" + name + ".txt"
    with open(file_name, "w") as file:
        file.write(age)


def print_average():
    sum_age = 0
    count_file = 0
    files = os.listdir("data")
    for file_name in files:
        with open("data\\" + file_name, "r") as file:
            age = file.read()
            age = int(age)
            sum_age = age + sum_age
            count_file = count_file + 1
    average = sum_age / count_file
    print("Average age is: {}".format(average))


def main():
    create_file()
    print_average()


main()
