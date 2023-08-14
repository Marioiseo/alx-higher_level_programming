#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        n = int(my_list[i])
        print("{}".format(n))
