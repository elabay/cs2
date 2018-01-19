#Elly Labay 1/17/18
#Read and complete Chapter 9.10 - 9.20
#Complete Exercise question #s 8, 12 and 22

# 8
def remove_ch(string, ch):
    num = len(string)
    remove_s =""
    for x in range (num):
        if string[x] != ch:
            remove_s += string[x]
    return remove_s

#12
def remove_string (string, d_string):
    num = len(d_string)
    start = string.find(d_string)
    if start < 0:
        return string
    final = string[:start] + string[start + num:]
    return final

#22
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            calc = 'Subtotal: ${:.2f}'.format(total)
            print(calc)
        else:
            moreItems = False
    average = total / count
    m_total = 'Total ${:.2f}'.format(total)
    a_total = 'Average price per item: ${:.2f}'.format(average)
    print('Total items:', count)
    print(m_total)
    print(a_total)

def main():
    print(remove_ch("Hello! My name is Elly. ", "l"))
    print (remove_string("Hello! My name is Elly. ", "Elly"))
    checkout()
main()
