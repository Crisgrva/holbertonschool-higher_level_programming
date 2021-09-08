#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

add = __import__("add_0").add
a = 1
b = 2
number = add(a, b)
print("{} + {} = {:d}".format(a, b, number))
