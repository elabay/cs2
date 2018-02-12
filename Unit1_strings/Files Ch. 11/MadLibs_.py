#Elly Labay 2/2/18

def mad_lists(data):
    #print(data)
    partofspeech = ["(time)", "(adj)", "(sound)", "(verb-past)", "(verb-ING)", "(adverb)","(noun)", "(verb-ED)", "(number)"]
    p_num = len(partofspeech)
    completed = ""
    line = data.split()
    i = 0
    for word in line:
        #print(word)
        if partofspeech[i] in line:
            place = line.index(partofspeech[i])
        #print(place)
            user = input(partofspeech[i])
            line[place] = user
          #  print(line)
           # if i == 5:
               # print (place)
        else:
            i +=1
            if i >=9:
                final = " ".join(line)
                return final
def mad_dic(data):
    partofspeech = ["(time)", "(adj)", "(sound)", "(verb-past)", "(verb-ING)", "(adverb)","(noun)", "(verb-ED)", "(number)" ]
    line = data.split()
    dic ={}
    replace = ""
    for i in partofspeech:
        user = input(i)
        dic[i] = user
    print(dic)
    for word in line:
        if dic[word] is True:
            print (dic[word])
            print [word]
            place = line.index(dic[word])
            line[place] = dic[word]
            print(line[word])
            print("true")
        else:
            replace += word
            print (replace)

   # final = " ".join(replace)
    return replace




def main():
    file = open("madlib_StrangeAnimal", "r")
    test_file = open("test d mad", "r")

    mad_temp = file.read()
    test = test_file.read()
    #print(mad_temp)

    #print(mad_lists(mad_temp))
    #print(mad_dic(mad_temp))
    print(mad_dic(test))


main()
