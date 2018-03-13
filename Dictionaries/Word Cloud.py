

import string

def clean(raw_data): # Clean the data making it all lowercase and taking out all punctuation
    Alph = string.ascii_lowercase
    raw_data = raw_data.lower()
    new_string =""
    for char in raw_data:
        if char in Alph:
            new_string+= char
        elif char in string.whitespace:
            new_string+= char
        elif char is "_":
            new_string+= " "
    newlo_string = new_string.lower()
    return newlo_string

def count_words(data_cleaned):
    line = data_cleaned.split()
    c_dic = {}
    for word in line:
        if word in c_dic:
            c_dic[word] += 1
        else:
            c_dic[word] = 1
    return c_dic

def longest(dictionary):
    sort_num ={}
    v_list = list(dictionary.values())
    k_list = list(dictionary.keys())
    
    for i in range(len(v_list)):
        sort_num[v_list[i]] = k_list[i]
        print (sort_num)

    return sort_num




def main():
    file = open("guido_vonRossum_speech.txt", "r")
    text = file.read()

    cleaned_text = clean("Hi my name is Elly Labay. My cats name is Oscar and my dogs name is Zooey.")

    dictionary_unsorted = count_words(cleaned_text)

    print(dictionary_unsorted)

    print(longest(dictionary_unsorted))
main()
