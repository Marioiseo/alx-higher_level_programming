#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        s = ord(str[i])
        a = str[i]
        if s >= 97 and s <= 122:
            s -= 32
            a = str(s)
        print("{}".format(a),end="")
    print("")            
