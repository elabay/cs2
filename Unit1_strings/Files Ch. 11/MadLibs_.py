#Elly Labay 2/2/18

def mad(data):
    partofspeech = ["(verb-ING)", "(adverb)","(noun)", "(verb-ED)", "(number)", "(unit of time)", "(adj)", "(sound)", "(verb-past)"]
    p_num = len(partofspeech)
    completed = ""
    for line in data:
        words = line.split()
        num = len(words)
        part_num = 0
        for i in range(p_num):
            if partofspeech[i] == words[]:
                user = input(partofspeech[i],": ")
            else:
                print(False)



def main():
    file = open("madlib_StrangeAnimal", "r")

    mad_temp = file.read()

    print(mad(mad_temp))


main()
