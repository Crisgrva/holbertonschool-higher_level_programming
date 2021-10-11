#!/usr/bin/python3
"""
8. Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        if self.integer_validator(width, width):
            self.__width=width

        if self.integer_validator(height, height):
            self.__height=height
