def main():
    line_number = 0
    file_name = input("Enter file name: ")
    if file_name.endswith(".txt"):
        with open(file_name, "r") as user_file:
            print("The lines with missing dot at the end are: ")
            for line in user_file:
                line = line.strip()
                line_number = line_number + 1
                if line.endswith("."):
                    pass
                else:
                    print("Line {}: ".format(line_number), line)
    else:



main()
