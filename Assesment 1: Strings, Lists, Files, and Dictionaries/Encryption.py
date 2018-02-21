#Elly Labay 2/21/18
import string

def encrypt(message):
    alph = string.ascii_lowercase
    new = ""
    for char in message:
        if char in string.whitespace:
            new += " "
        if char in alph:
            place = alph.find(char)
            n_char = place - 6
            new += alph[n_char]
    return new


def main():
   print(encrypt("hello world"))

main()

