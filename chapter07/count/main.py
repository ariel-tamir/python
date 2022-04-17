def main():
    count = 0
    all_lines = 0
    with open("input.txt", "r") as my_file:
        for line in my_file:
            all_lines = all_lines + 1
            if "mirabel" in line.lower():
                count = count + 1
                print(line)
        print("{} lines located".format(count))
        print("there are {} lines".format(all_lines))


main()
