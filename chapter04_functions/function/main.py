from random import randint


def play(lowest, highest, bet):
    selected = randint(lowest, highest)

    if selected == bet:
        print("You win!!")
        return True
    else:
        print("You lose!")
        return False


def main():
    highest = input("write the highest number: ")
    lowest = input("write the lowest number: ")
    bet = input("write bet: ")

    highest = int(highest)
    lowest = int(lowest)
    bet = int(bet)

    points = 0

    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1
    win = play(lowest, highest, bet)
    if win:
        points = points + 1

    win = play(lowest, highest, bet)
    if win:
        points = points + 1

    win = play(lowest, highest, bet)
    if win:
        points = points + 1

    print("your points: {}".format(points))


main()
