#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if i == 0:
            print("{:d}".format(my_list[-1]))
        else:
            print("{:d}".format(my_list[-i - 1]))