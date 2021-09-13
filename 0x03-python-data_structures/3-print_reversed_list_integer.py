#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(len(my_list))):
        if my_list[i] == None:
            print("None")
        else:
            print("{:d}".format(my_list[i]))
