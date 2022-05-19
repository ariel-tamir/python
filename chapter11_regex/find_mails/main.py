import re


def find_mail():
    with open("input.txt", "r") as my_file:
        for line in my_file:
            mails = re.findall(r"\w+\S\w+@\w+\S\w+", line)
            for mail in mails:
                print(mail)


def confidence():
    sum_numbers = 0
    count_file = 0
    with open("input.txt", "r") as my_file:
        for line in my_file:
            x = re.findall(r"X-DSPAM-Confidence:\s(\d\.\d+)", line)
            for number in x:
                number = float(number)
                sum_numbers = number + sum_numbers
                count_file = count_file + 1
    average = sum_numbers / count_file
    print(average)


find_mail()
confidence()
