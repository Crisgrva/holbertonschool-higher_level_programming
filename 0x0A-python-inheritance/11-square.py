#!/usr/bin/python3
"""
11. Square #2
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Write a class Square that inherits from
    Rectangle (9-rectangle.py). (task based on 10-square.py).
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return(self.__size * self.__size)

    def __str__(self):
        return ('[Square] {}/{}'.format(self.__size, self.__size))
