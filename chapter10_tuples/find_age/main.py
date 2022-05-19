def read_name():
    names = {}
    with open("disney.txt", "r") as my_file:
        for line in my_file:
            line = line.strip()
            words = line.split(",")
            name = (words[0], words[1])
            age = words[2]
            names[name] = age
    return names


def answer(names):
    ans = input("Enter name: ")
    name = ans.split()
    name = (name[0], name[1])
    age = names[name]
    print("The age is: {}".format(age))


def main():
    name = read_name()
    answer(name)


main()
