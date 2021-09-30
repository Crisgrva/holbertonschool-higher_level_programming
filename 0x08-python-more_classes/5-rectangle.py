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
        return(self.__height * self.__width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        str_print = ""

        if self.__width == 0 or self.__height == 0:
            return str_print
        h = 1
        while h <= self.__height:
            str_print += "#" * self.__width
            if h < self.__height:
                str_print += "\n"
            h += 1
        return str_print

    def __del__(self):
        print("Bye rectangle...")

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)
        return "Rectangle(" + width + ", " + height + ")"
