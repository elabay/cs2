#Elly Labay 1/29/30

def replace (string, old, new):
    erased = string.split(old)
    glue = new
    together = glue.join(erased)
    return together




def main():

    file = open("Strings_lists_tuples_elly", "r")

    data = file.read()
    #print(data)
   # print(replace('I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!', "om", "am"))
    print(replace(data, "i", "I"))
    print(replace(data, "a", "AA"))

main()
