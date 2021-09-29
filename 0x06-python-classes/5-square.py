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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    def my_print(self):
        x = 0
        y = 0
        if self.__size == 0:
            print()
        for x in range(0, self.__size):
            for y in range(0, self.__size):
                print("#", end="")
            print()
