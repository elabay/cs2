#Elly Labay 2/2/18
import time

def mad_lists(data,partofspeech):
    #print(data)
    p_num = len(partofspeech)
    completed = ""
    line = data.split()
    num = len(line)
    i = 0
    for word in line:
        #print(word)
        if partofspeech[i] in line:
            place = line.index(partofspeech[i])
        #print(place)
            user = input(partofspeech[i])
            line[place] = user
            print(i)
        else:
            i +=1
            if i >=11:
                final = " ".join(line)
                return final



def mad_dic(data, partofspeech):
    line = data.split()
    dic ={}
    #replace = ""
    for i in partofspeech:
        user = input(i)
        dic[i] = user
    #print(dic)
    for word in line:
        if word in dic:
            #print (dic[word])
           # print [word]
            place = line.index(word)
            line.insert(place, dic[word])
            #line[place] = dic[word]
           # print(line[word])
           # print(word)
            print(word)
        else:
            print(9435678)
            time.sleep(5)
            None


    final = " ".join(line)
    print(final)

def d_mad(data, partofspeech):
    dic ={}
    for i in partofspeech:
        user = input(i)
        dic[i] = user


    return






def main():
    parts = ["(adj)","(sounds)", "(sound)", "(verb-past)", "(verb-ING)", "(adverb)","(noun)", "(verb-ED)", "(number)", "-(adj)", "-(verb-ED)"]
    file = open("madlib_StrangeAnimal", "r")
    test_file = open("test d mad", "r")

    mad_temp = file.read()
    test = test_file.read()
    #print(mad_temp)

    #print(mad_lists(mad_temp,parts))
    print(mad_dic(mad_temp, parts))
   # print(mad_dic(test))

   # print( d_mad(mad_temp, parts))
    #print(type(mad_temp))
main()
