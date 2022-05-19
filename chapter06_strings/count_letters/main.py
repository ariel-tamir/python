def count_letters(sentence, find_letter):
    times = 0
    for char in sentence:
        if char == find_letter:
            times = times + 1
    print("{} amount: {}".format(find_letter, times))


def main():
    sentence = input("Enter your sentence: ")
    count_letters(sentence, "a")
    count_letters(sentence, "b")
    count_letters(sentence, "c")


main()
