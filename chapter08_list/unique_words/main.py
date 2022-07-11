def main():
    all_words = []
    with open("input.txt", "r") as my_file:
        for line in my_file:
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in all_words:
                    all_words.append(word)
    all_words.sort()
    print(all_words)


main()
