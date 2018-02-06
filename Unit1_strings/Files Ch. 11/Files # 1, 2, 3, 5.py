# Elly Labay 2/1/18
import string
import turtle
import math

def score_name(data):
    for line in data:
        list_score = line.split()
        if len(list_score) > 7:
            print(list_score[0])

def average_score(data):
    for line in data:
        list_score = line.split()
        total = 0
        grades =list_score [1: ]
        for grade in grades:
            total = total + int(grade)
        av_score = (total/(len(grade)))
        print (list_score[0], av_score )


def min_max (data):
    for line in data:
        print(line)
        #print(type(data))
        list_score = line.split()
        print(type(list_score))
        print(min(list_score[1:]))
        print(max(list_score[1:]))
        print(list_score[0], min(list_score[1:]),  max(list_score[1:]))

def draw(t, f):
    for aline in f:
        items = aline.split()
        if items[0] == "UP":
            t.up()
        else:
            if items[0] == "DOWN":
                t.down()
            else:
                t.goto(int(items[0]), int(items[1]))

def main():
    fin = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-300, -300, 300, 300)

    data_stu = open("studentdata.txt")
    text = open('mystery.txt')

    #file = text.read()
    #print(type(data))
    #score_name(data_stu)
   # average_score(data_stu)
    min_max(data_stu)
    #draw(fin, text)

    text.close()
    data_stu.close()


main()



