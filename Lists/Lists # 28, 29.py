# Elly Labay 1/28/18
import turtle

def LSystem29(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString29(startString)
        startString = endString

    return endString

def LSystem28(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString28(startString)
        startString = endString

    return endString

def processString29(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Rules29(ch)

    return newstr

def processString28(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Rules28(ch)

    return newstr

def Rules29(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F[-F]F[+F]F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def Rules28(ch):
    newstr = ""
    if ch == 'H':
        newstr = 'HFX[+H][-H]'   # Rule 1
    elif ch == 'X':
        newstr = 'X[-FFF][+FFF]FX'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem29(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            #print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

def drawLsystem28(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'H':
            aTurtle.forward(distance)
        elif cmd == 'X':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            #print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

def draw_image(draw, t, inst, angle, length, wn):
        t.up()
        t.back(200)
        t.down()
        t.speed(0)
        draw(t, inst, angle, length)
        wn.exitonclick()


def main():
    wn = turtle.Screen()
    fin = turtle.Turtle() # creates the turtle

    #28
    inst = LSystem28(4, "H")   # create the string
    print(inst)
    draw_image(drawLsystem28,fin,inst, 25.7, 5, wn)

#29
    inst = LSystem29(4, "F")   # create the string
    print(inst)
    draw_image(drawLsystem29,fin,inst, 25, 5, wn)



main()
