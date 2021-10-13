#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


class pascal_triangle:
    """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """
    def __init__(self, size):
        self.size = size
        self.matrix = []
        for line in range(0, self.size):
            for i in range(0, line + 1):
                self.matrix.append((self.binomialCoeff(line, i)))

        print(self.matrix)


    def binomialCoeff(self, n, k) :
        res = 1
        if (k > n - k) :
            k = n - k
        for i in range(0 , k) :
            res = [res * (n - i)]
            res = [res // (i + 1)]
     
        return res

    def __iter__(self):
        return self.matrix


