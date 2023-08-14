#!/usr/bin/python3

if __name__== "__main__":
    import sys
    argv = sys.argv[1:]
    arglen = len(argv)
    num = int(argv[0])
    for i in range(1, arglen):
        num += int(argv[i])
    print(num)
