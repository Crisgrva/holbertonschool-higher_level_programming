#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for element in range(0, len(list)):
            print("{}".format(list[element]), end="")
            if element != len(list) - 1:
                print("{}".format(" "), end="")
        print("{}".format(""))
