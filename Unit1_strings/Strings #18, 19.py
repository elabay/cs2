#Elly Labay 1/19/18 encrypts and decrypts a text file

#18
def encrypt(e_f):
    #alphabet_upper = ["A", 'B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P','Q','R', 'S','T','U','V', 'W', 'X','Y','Z', " "]
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z', ' ', ';',':' ,'.', "'", '-', '(',')', '!', '\n', ",", "?"]
    alphabet_replace = ['p', 'q', 'r', 's', 't','u','a', 'b', 'c', 'd', 'e', 'f','v', 'w', 'x', 'y', 'z', ' ', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',';',':','.',"'" , '-', '(',')', '!', "\n", ",", "?"]
    num = len(e_f)
    o_file = e_f.lower()
    print(o_file)
    old_char = True
    n_file= " "
    for t_char in range (num):
        a_compare = 0
        old_char = True
        while old_char == True:
            #print("t",t_char)
            #print("a",a_compare)
            if o_file[t_char] == alphabet_lower[a_compare]:
                n_char = alphabet_replace[a_compare]
                #n_file = o_file.replace(o_file[t_char], n_char)
                n_file += n_char
                #print("n",n_char)
                #print (o_file)
                #print (n_file)
                old_char = False
               # print (old_char)
            else:
                a_compare += 1


    return  o_file, n_file

#19
def decrypt(d_f):
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z', ' ', ';',':' ,'.', "\'", '-', '(',')', '!', '\n', ',', "?"]
    alphabet_replace = ['p', 'q', 'r', 's', 't','u','a', 'b', 'c', 'd', 'e', 'f','v', 'w', 'x', 'y', 'z', ' ', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',';',':','.', "\'", '-', '(',')', '!', "\n", ',',"?"]
    num = len(d_f)
    d_file = d_f.lower()
    d_char = True
    n_file= " "
    for t_char in range (num):
        a_compare = 0
        d_char = True
        while d_char == True:
           # print("t",t_char)
            #print("a",a_compare)
            if d_file[t_char] == alphabet_replace[a_compare]:
                n_char = alphabet_lower[a_compare]
                #n_file = o_file.replace(o_file[t_char], n_char)
                n_file += n_char
               # print("n",n_char)
               # print (d_file)
                #print (n_file)
                d_char = False
                #print (old_char)
            else:
                a_compare += 1
    return n_file



def main():
    file_r = open("guido_vonRossum_speech.txt", "r")
    #file_w = open("guido_vonRossum_speech.txt", "w")

    data_r = file_r.read()
    #data_w = file_w.write()
   # print(encrypt("hi my name is elly"))
    #print(decrypt("bcovmowpvtocgotffm"))
   # print(data_r)
    print(encrypt(data_r))

main()
