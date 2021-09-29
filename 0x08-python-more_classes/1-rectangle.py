#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """Empty class Square that defines a rectangle.
    Starting to use Comments in Python
    """
    def __init__(self, width=0, height=0):
        ispw = isinstance(width, int)
        isph = isinstance(height, int)

        if ispw is False:
            raise Exception("width must be an integer")
        elif isph is False:
            raise Exception("height must be an integer")

        if height < 0:
            raise Exception("height must be >= 0")
        elif width < 0:
            raise Exception("width must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
