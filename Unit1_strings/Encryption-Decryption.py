# Elly Labay 1/25/18
import string
def encrypt(f_f):
    n_file = " "
    Alph = string.ascii_lowercase
    R_Alph = "mnbvcxzlkjhgfdsapoiuytrewq"
    o_file = f_f.lower()
    num= len(o_file)
    space_count = o_file.count(string.whitespace)
    space = True
    for s in range (num):
        if o_file[s] == string.whitespace:
            n_file += "."
        if o_file[s] == Alph[s]:
            n_char = R_Alph[s]
            n_file += n_char



