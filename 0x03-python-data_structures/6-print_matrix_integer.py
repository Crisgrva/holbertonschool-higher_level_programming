#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for element in range(len(list)):
            print("{:d}".format(list[element]), end="")
            if element != len(list) - 1:
                print("{}".format(" "), end="")
        print("{}".format(""))
