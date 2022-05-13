import random


def generate_word():
    letters = "abc"
    word = ""
    word_length = random.randint(2, 5)
    for m in range(word_length):
        letter = random.choice(letters)
        word = word + letter
    return word


def main():
    word = generate_word()
    guess = input("Enter your guess: ")
    a = 0
    while guess != word:
        a = a + 1
        if guess > word:
            print("Wrong, your guess is too high")
        else:
            print("Wrong, your guess is too low")
        guess = input("Enter your guess: ")

        if word.startswith(guess):
            print("This is a good prefix!")
    print("Correct!!! You Win!!!")
    print("Total of {} guesses".format(a))


main()
