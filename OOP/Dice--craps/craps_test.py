import random


def roll():
    input("Press Enter to roll")
    dice = random.randint(1, 6), random.randint(1, 6)
    print("You rolled a {}" .format(dice))
    return sum(dice)


def check_roll(dice, win_conditions=(7, 11), lose_conditions=(2, 3, 12)):
    if dice in win_conditions:
        print("You win")
        start_game()
    elif dice in lose_conditions:
        print("You lose")
        start_game()
    else:
        print("Time to try to roll the point")
        check_roll(roll(), (dice,), (7,))


def start_game(first_run=False):
    if first_run:
        print("Do you wanna play Craps? Y/n ")
        response = input(">>> ")
    else:
        response = input("Play Again? Y/n >>>")
    if response.lower() == "y":
        check_roll(roll())
    else:
        input("ENTER to quit")


if __name__ == '__main__':
    start_game(True)
