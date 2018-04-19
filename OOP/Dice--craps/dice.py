import random

class Dice:
    """Implements a collection of dice, as changing numbers."""
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = random.randrange(1,7)

    def rollAll(self):
       self.roll(range(5))


    def values(self):
        return self.dice[:]

    def score(self):
        goal = 0
        for value in self.dice:
            start =+ value
        goal = start
        return goal




