#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            s = ord(str[i])
            s -= 32
        print(f"{str(s)}",end="")
    print("")            
