#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """Empty class Square that defines a rectangle.
    Starting to use Comments in Python
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        str_print = ""

        if self.width == 0 or self.height == 0:
            return str_print

        for h in range(self.height + 1):
            str_print += "#" * self.width
            if h < self.height:
                str_print += "\n"
        return str_print
