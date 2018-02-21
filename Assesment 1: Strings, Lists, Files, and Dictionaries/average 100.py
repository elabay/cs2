#Elly Labay 2/21/18 creates a list of 100 random numbers (0-1000) and then gets the average of those numbers
import random
def create_100():
    list = []
    for i in range(100):
        num = random.randrange(0,1001)
        list.append(num)
    return list


def average(list):
    sum = 0
    for num in list:
        sum +=num
    total = len(list)
    av = sum/total
    return av


def main():
    #print(create_100())
    #list =[1,2,3]
    #print(average(list))
    print(average(create_100()))
main()
