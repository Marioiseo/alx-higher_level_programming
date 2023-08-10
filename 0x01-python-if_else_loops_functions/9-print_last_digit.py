#!/usr/bin/python3
def print_last_digit(number):
    s = abs(number)
    s %= 10
    print("{}".format(s),end="")
    return s
