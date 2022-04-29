def remove_second_from_list(my_list):
    del my_list[1]


def remove_second_from_tuple(my_tuple):
    return my_tuple[0], my_tuple[2]


def main():
    numbers = [2, 5, 6, 8, 7]
    remove_second_from_list(numbers)
    print(numbers)

    name = ("Ariel", "Mirabel", "Tamir")
    name2 = remove_second_from_tuple(name)
    print(name2)


main()
