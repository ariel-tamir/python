def read_words():
    words_count = {}
    with open("input.txt", "r") as my_file:
        for line in my_file:
            line = line.lower()
            words = line.split()
            for word in words:
                if word in words_count:
                    words_count[word] = words_count[word] + 1
                else:
                    words_count[word] = 1
    return words_count


def print_words(counters):
    for word, count in counters.items():
        print(word, count)


def main():
    counts = read_words()
    print_words(counts)


main()
