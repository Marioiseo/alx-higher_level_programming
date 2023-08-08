#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nummod = abs(number) % 10
if number < 0:
    nummod = nummod * -1
if nummod == 0:
    print(f"last digit of {number} is {nummod} and is 0")
elif nummod > 5:
    print(f"last digit of {number} is {nummod} and is greater than 5")
else:
    print(f"last digit of {number} is {nummod} and is less than 6 and not 0")
