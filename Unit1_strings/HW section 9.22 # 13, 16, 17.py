# Elly Labay 1/25/18 L-systems drawing with turtles
import turtle

def LSystem13(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString13(startString)
        startString = endString

    return endString

def LSystem14(numIters, axiom):
   # print("createLSystem14 check")
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString14(startString)
        startString = endString

    return endString

def LSystem17(numIters, axiom):
   # print("createLSystem14 check")
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString17(startString)
        startString = endString

    return endString

def processString13(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Rules13(ch)

    return newstr

def processString14(oldStr):
   # print("ProcessString14 check")
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Rules14(ch)

    return newstr

def processString17(oldStr):
   # print("ProcessString14 check")
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Rules17(ch)

    return newstr

def Rules13(ch):
    newstr = ""
    if ch == 'L':
        newstr = '+RF-LFL-FR+'   # Rule 1
    elif ch == 'R':
        newstr = '-LF+RFR+FL-'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def Rules14(ch):
   # print("applyRules14 check")
    newstr = ""
    if ch == 'X':
        print(3)
        newstr = 'X+YF+'   # Rule 1
    elif ch == 'Y':
        newstr = '-FX-Y'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def Rules17(ch):
   # print("applyRules14 check")
    newstr = ""
    if ch == 'F':
        print(3)
        newstr = 'FF'   # Rule 1
    elif ch == 'X':
        newstr = '--FXF++FXF++FXF--'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem13(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def drawLsystem14(aTurtle, instructions, angle, distance):
   # print("drawLSystem14 check")
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def drawLsystem17(aTurtle, instructions, angle, distance):
   # print("drawLSystem14 check")
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def draw_image(t, inst, angle, length, wn):
        t.up()
        t.back(200)
        t.down()
        t.speed(9)
        drawLsystem13(t, inst, angle, length)
        wn.exitonclick()


def main():
    wn = turtle.Screen()
    fin = turtle.Turtle() # creates the turtle

#13
   # inst = LSystem13(4, "R")   # create the string
   # print(inst)
    #draw_image(fin,inst, 90, 5, wn)

#14
    print(333)
    inst = LSystem14(10, "X")   # create the string
    print(inst)

    draw_image(fin,inst, 90, 5, wn)

#17
    print(333)
    inst = LSystem17(4, "FXF--FF--FF")   # create the string
    print(inst)
    draw_image (fin, inst, 60, 5, wn)



main()
