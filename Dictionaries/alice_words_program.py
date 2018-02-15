#Elly Labay
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


def sorted_dictionary(old_dic, list):
    new_dic={}
    for word in list:
        if word in old_dic:
            value = old_dic[word]
            new_dic[word] = value
    return new_dic


def word_finder(dictionary):
    user = input("What word would you like to search for: ")
    word_count= dictionary[user]
    return word_count


def main():
    #file = open("test Text file_Guillotine", "r")
    file = open("Alice in Wonderland", "r")
    text = file.read()


    cleaned_text = clean(text)

    dictionary_unsorted= count_words(cleaned_text)
    list_sorted = sorted(dictionary_unsorted)
    final_d = sorted_dictionary(dictionary_unsorted,list_sorted )
    #print(final_d)

   # print(word_finder(final_d))
   # text.close()
    new_file = open("alice_words","w")
    for k in final_d:
        new_file.write("{0}:{1}".format(k, final_d[k])+ '\n')


main()
