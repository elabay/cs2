# dieview_list.py
from graphics import *

class DieView_List:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
        d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""
        # first define some standard values
        self.win = win
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size # radius of each pip
        hsize = size / 2.0 # half of size
        offset = 0.6 * hsize # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [self.__make_pip(cx - offset, cy - offset),
                     self.__make_pip(cx - offset, cy),
                     self.__make_pip(cx - offset, cy + offset),
                     self.__make_pip(cx, cy),
                     self.__make_pip(cx + offset, cy - offset),
                     self.__make_pip(cx + offset, cy),
                     self.__make_pip(cx + offset, cy + offset)]

        # Create a table for which pips are on for each value
        self.onTable = [ [], [3], [2,4], [2,3,4],
        [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6] ]

        self.set_value(1)

    def __make_pip(self, x, y):
        """Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def set_value(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        self.value = value
        for pip in self.pips:
            pip.setFill(self.background)
        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

    def set_color(self, color):
        """Change the color of a die to indicate whether it is selected for rerolling."""
        self.foreground = color
        self.set_value(self.value)

    def set_dice(self, values):
        for i in range(5):
            self.dice[i].set_value(values[i])

    def want_to_play(self):
        ans = self.choose(["Roll Roller", "Quit"])
        self.msg.setText("")
        return ans == "Roll Roller"
