#!/usr/bin/python3
def pow(a, b):
    c = a
    for i in range(0, b):
        if b > 0:
            c = c * a
        if b < 0:
            c = c / a
    return c
