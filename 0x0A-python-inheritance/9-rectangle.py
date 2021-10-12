#!/usr/bin/python3
"""
9. Full rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py).
    (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return(self.__height * self.__width)

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
