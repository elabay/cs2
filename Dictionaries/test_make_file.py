import turtle
import string

def clean(text): # Clean the data making it all lowercase and taking out all punctuation
    Alph = string.ascii_lowercase
    text = text.lower()
    new_string =""
    for char in text:
        if char in Alph:
            new_string+= char
        elif char in string.whitespace:
            new_string+= char
        elif char is "_":
            new_string+= " "
    newlo_string = new_string.lower()
    return newlo_string


def main():
    #print(clean("Test Text file_Guillotine"))
    d = {'a':1, 'c':2, 'b':3}
    d_s ={}
    print(sorted(d))
    for k in sorted(d):
        d_s += "{0}: {1}".format(k,d[k])
    print(d_s)

main()
