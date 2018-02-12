import string
def clean(text):
    #num =len(text)
    Alph = string.ascii_lowercase
    new_string= ""
    for char in text:
        if char in Alph:
            new_string+= char
    newlo_string = new_string.lower()
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
            print(letter)
            value = old_dic[letter]
            print(value)
            new_dic[letter]+= value
    print (old_dic)
    return new_dic


def main():
    file = open("Test Text file_Guillotine", "r")
    text_file = file.read()
    diction = countAll(clean(text_file))
    list= sort_list(countAll(clean(text_file)))
    print(diction)
    print(list)
    print(sorted_dict(diction, list))
    #print((clean(text_file)))
   # print(list)
main()
