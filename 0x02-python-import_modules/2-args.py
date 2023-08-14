#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    filename = sys.argv[0]
    arguments = sys.argv[1:]
    arglen = len(arguments)
    if arglen > 1:
        print("{} arguments:".format(arglen))
        for i in range(0, arglen):
            print("{}: {}".format(i + 1, arguments[i]))
    elif arglen == 1:
        print("{} argument:".format(arglen))
        print("1: {}".format(arguments[0]))
    else:
        print("0 arguments.")
