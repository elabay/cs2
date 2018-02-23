#Elly Labay 2/21/18

def longest(data):
    line = data.split()
    num = {}
    for word in line:
        length = len(word)
        num[word] = length
    v_list = list(num.values())
    k_list = list (num.keys())
    longest_num = max(v_list)
    place = v_list.index(longest_num)
    word = k_list[place]
    return word, longest_num






def main():
    file = open("science daily", "r")
    text = file.read()
    #print(longest("hi my name is"))
    print(longest(text))


main()

