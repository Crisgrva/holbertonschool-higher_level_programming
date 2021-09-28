#!/usr/bin/python3
"""3. Area of a square"""


class Square:
    """Write a class Square that defines a square by:
    (based on 2-square.py)
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise Exception("size must be an integer")
        elif size < 0:
            raise Exception("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
