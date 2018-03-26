# face.py
from graphics import *
from graphics import Circle
from graphics import Line
from graphics import Point
from graphics import GraphWin
from graphics import Polygon

class Face:

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)

    def Move(self, dx, dy):
        for p in self.points:
            p.Move(dx,dy)

    def Flinch (self, center, size, window):
        eyesize = 0.15 * size
        eyeOff = size / 3.0
        self.leftEye = Line(Point(center.x + eyesize/2, center.y), Point(center.x - eyesize/2, center.y))
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyesize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)



def main():
    win = GraphWin("Face", 500, 500)
    Face(win, Point(50,50), 30)

stay =1
while stay == 1:
    main()
