import re


def main():
    number = input("Enter number: ")
    match = re.findall(r"^\d+(\.\d+)?$", number)
    if len(match) == 1:
        print("valid")
    else:
        print("invalid")


main()
