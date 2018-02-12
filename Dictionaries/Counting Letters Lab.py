def countAll(data):
    c_dic = {}
    for count in data:
        if count in c_dic:
            c_dic[count] += 1
        else:
            c_dic[count] = 1
    return c_dic


def main():
    file = open("test Text file_Guillotine", "r")
    text = file.read()

    print(countAll(text))

main()
