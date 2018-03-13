# Elly Labay taking a string counting and storing the number of occurances of the letters and then making a histogram of the letter values with dictionaries
import turtle
import string

def clean(text): # Clean the data making it all lowercase and taking out all punctuation
    Alph = string.ascii_lowercase
    space = string.whitespace
    new_string =""
    for char in text:
        if char in Alph:
            new_string+= char
    newlo_string =new_string.lower()
    return newlo_string

def countAll(data):
    c_dic = {}
    for count in data:
        if count in c_dic:
            c_dic[count] += 1
        else:
            c_dic[count] = 1
    return  c_dic

def sort_list(dic):
    s_keys = list(dic.keys())
    s_keys.sort()
    return s_keys

def sorted_dict(old_dic, list):
    new_dic={}
    for letter in list:
        if letter in old_dic:
            #print(letter)
            value = old_dic[letter]
           # print(value)
            new_dic[letter] = value
    return new_dic


def barChart(t, value, letter):
    t.pensize(3)
   # t.speed (0)
    t.fillcolor("blue")
    t.begin_fill()
    t.left(90)
    t.forward(value)
    t.right(90)
    t.forward(20)
    t.write(str(value), align="left", font = ("Arial", 13, "normal"))
    t.forward(30)
    t.right(90)
    t.forward(value)
    t.left(90)
    t.end_fill()
    t.penup()
    t.backward(25)
    t.write(str(letter), align="left", font = ("Arial", 20, "normal"))
    t.forward(25)
    t.pendown()
    t.forward(30)


def main():
    wn = turtle.Screen()
    fin = turtle.Turtle()
    fin.shape("turtle")
    file = open("Alice in Wonderland", "r")
    text_file = file.read()
    diction = countAll(clean(text_file))
    list = sort_list(countAll(clean(text_file)))

    data = sorted_dict(diction, list)
    data_num = data.values()
    largest_data = max(data_num)
    data_points = len(data_num)

    border = 25
    wn.setworldcoordinates(0-border, 0-border, 50*data_points+border, largest_data+border+30)

    for i in data:
       # print (i, data[i])
        barChart(fin, data[i], i)

main()
