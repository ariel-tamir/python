from datetime import datetime


def main():
    name = input("file name: ")
    name = name + ".txt"
    with open(name, "w") as file:
        time = datetime.now()
        time = str(time)
        file.write(time)


main()
