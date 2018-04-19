from graphics import *
from dieview_list import DieView_List
from button import Button


class CrapsInterface:
    def __init__(self, goal, total):
        self.win = GraphWin("Dice Craps", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(420,50), "CRAPS")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.msg = Text(Point(420,75), "Welcome to the Dice Table")
        self.msg.setSize(14)
        self.msg.draw(self.win)

        self.msg = Text(Point(170,40),goal )
        self.msg.setSize(30)
        self.msg.draw(self.win)

        self.msg = Text(Point(170, 350), total)
        self.msg.setSize(30)
        self.msg.draw(self.win)



        self.create_dice(Point(320, 150), 75)

        self.buttons = []

        self.add_dice_buttons(Point(320, 200), 75, 30)

        b = Button(self.win, Point(420, 230), 400, 50, "Roll Dice")
        self.buttons.append(b)


        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)

        #self.money = Text(Point(420,325), "$100")
       # self.money.setSize(18)
        #self.money.draw(self.win)

    def choose(self, choices):
        buttons = self.buttons
        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        # get mouse clicks until an active button is clicked
        while 1:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() # function exit here.

    def create_dice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(2):
            view = DieView_List(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def add_dice_buttons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,3):
            label = "Die %d" % (i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def set_money(self, amt):
        self.money.setText("$%d" % (amt))

    def show_result(self, msg, score):
        if score > 0:
            text = "%s! You win $%d" % (msg, score)
        else:
            text = "You rolled %s" % (msg)
        self.msg.setText(text)

    def set_dice(self, values):
        for i in range(2):
            self.dice[i].set_value(values[i])

    def want_to_play(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

