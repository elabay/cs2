import random

def num():
    start = 0
    stop = 100
    goal_num = int(random.randrange(start,stop))
    return goal_num

def game(number):
    starting = input("Are you Ready to Play?  ")
    if starting == "Yes" or "yes" or " Yes" or " yes":
        for lives in range (5):
            for players in range(2):
                if players == 0:
                    player_1 = int(input("Player 1, please guess a number between 0 and 100. Your Guess: "))
                    if player_1 == number:
                        return ("You Won!")
                    elif player_1 >= number:
                        print ("Your Number is too high")
                    elif player_1 <= number:
                        print ("Your Number is too low")
                    else:
                        print("Player 1, you have inputed an invalid answer you have lost your turn")
                if players == 1:
                    player_2 = int(input("Player 2, please guess a number between 0 and 100. Your Guess: "))
                    if player_2 == number:
                        return ("You Won!")
                    elif player_2 >= number:
                        print ("Your Number is too high")
                    elif player_2 <= number:
                        print ("Your Number is too low")
                    else:
                        print("Player 2, you have inputed an invalid answer you have lost your turn")

def main():
    print (game(num()))

    playback = input ("Would you like to play again? ")

    if playback == "Yes":
        print (game(num()))
    else:
        print("Bummer, you can run the program again if you want to play")



main()
