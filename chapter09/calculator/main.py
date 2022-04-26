def calc():
    words_count = {}

    with open("input.txt", "r") as my_file:
        for line in my_file:
            words = line.split()
            command = words[0]
            word = words[1]
            if command == "ADD":
                if word in words_count:
                    words_count[word] = words_count[word] + 1
                else:
                    words_count[word] = 1
            elif command == "REMOVE":
                words_count[word] = words_count[word] - 1
    return words_count


def print_words(counters):
    for word, count in counters.items():
        if count != 0:
            print(word, count)


def main():
    counts = calc()
    print_words(counts)


main()
