#!/usr/bin/python3
import add_0
add = __import__("add_0").add
a = 1
b = 2
number = add(a, b)
print("{} + {} = {:d}".format(a, b, number))
