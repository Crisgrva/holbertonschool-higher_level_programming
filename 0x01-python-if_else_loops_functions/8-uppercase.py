#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = ord(i)
        if upper >= 97 and upper <= 122:
            upper -= 32
        print("{:c}".format(upper), end="")
    print()
