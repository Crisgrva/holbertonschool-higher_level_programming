#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

sign = ""

if (number < 10):
    sign = "-"

if (number % 10) > 5:
    str = "and is greater than 5"
elif (number % 10) == 0:
    str = "and is 0"
elif ((number % 10) < 6) and ((number % 10) != 0) :
    str = "and is less than 6 and not 0"

strpr = "Last digit of {:d} ".format(number) + "is " + sign + "{:d} ".format(number % 10) + str

print(strpr)
