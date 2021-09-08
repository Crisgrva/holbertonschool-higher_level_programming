#!/usr/bin/python3
for x in range(0, 10):
    for i in range((x + 1), 10):
        if (x == 8 and i == 9):
            print("{:d}{:d}".format(x, i), end='')
        else:
            print("{:d}{:d}, ".format(x, i), end='')
