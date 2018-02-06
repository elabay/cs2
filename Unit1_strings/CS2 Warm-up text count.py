import string

def word_count(text):
    listed_text = text.split()
    num =len(listed_text)
    unique_words = " "
    u_count = 0
    for i in range (num):
        if listed_text[i] not in unique_words:
            unique_words += listed_text[i]
            unique_words += " "

    for count in range (num):
        if unique_words[u_count] == listed_text [count]:




    return unique_words

def clean(text):
    #num =len(text)
    Alph = string.ascii_lowercase
    new_string= ""
    for char in text:
        if char not in string.punctuation:
            new_string+= char
    newlo_string = new_string.lower()
    return newlo_string




def main():

    file = open("Strings_lists_tuples_elly", "r")

    data = file.read()
    #print(data)
    #print(word_count(data))
    print (word_count(clean (data)))

main()
