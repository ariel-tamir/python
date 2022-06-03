file_name = input("Enter file name: ")

def missing_dot():
    line_number = 0
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


def average():


missing_dot()
