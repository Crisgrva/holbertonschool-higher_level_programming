#!/usr/bin/python3
"""
1. Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Write a function that divides all elements of a matrix.
    """

    """Error Messages"""
    tpe_err = "matrix must be a matrix (list of lists) of integers/floats"
    sze_err = "Each row of the matrix must have the same size"
    dvi_err = "div must be a number"
    dvi_zero_err = "division by zero"

    if div == 0:
        raise ZeroDivisionError(dvi_zero_err)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(dvi_err)
    if not isinstance(matrix, list):
        raise TypeError(tpe_err)
    if len(matrix) == 0:
        raise TypeError(tpe_err)

    new_matrix = []
    
    if isinstance(matrix[0], bool):
        raise TypeError(tpe_err)
    try:
        len_fst_row = len(matrix[0])
    except Exception:
        raise TypeError(tpe_err)

    for lista in matrix:

        if not isinstance(lista, list):
            raise TypeError(tpe_err)

        for element in lista:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(tpe_err)
            if isinstance(element, bool):
                raise TypeError(tpe_err)

        if len(lista) != len_fst_row:
            raise TypeError(sze_err)

        new_matrix.append(list(map(lambda n: round(n/div, 2), lista)))

    return new_matrix
