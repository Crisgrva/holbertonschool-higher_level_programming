#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[num**2 for num in list] for list in matrix]
    return new_matrix
