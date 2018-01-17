def reverse(astring):
    r_string = ""
    num = len(astring)
    for x in range(num):
        r_string += astring[num - x - 1]
    return r_string
astring = "hello"
print( reverse(astring) )


