#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        s = ord(str[i])
        if s >= 97 and s <= 122:
            s -= 32
        print("{:s}".format(str(s)),end="")
    print("")            
