
from dice import Dice

class CrapsApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.want_to_play():
            self.playRound()
        self.interface.close()

    def playRound(self):
        self.doRolls()
        result, score = self.dice.score()
        self.interface.show_result(result, score)



    def doRolls(self):
        print(self.dice.rollAll())
        goal = self.dice.values()
        if goal == 7:
           print ("win")
        elif goal == 2:
            print ("lose")
        else:
            return goal






