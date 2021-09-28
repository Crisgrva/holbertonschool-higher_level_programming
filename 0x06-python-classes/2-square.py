#!/usr/bin/python3
"""1. Square with size"""


class Square:
    """Write a class Square that defines a square by:
        (based on 0-square.py)"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise Exception("size must be an integer")
        elif size < 0:
            raise Exception("size must be >= 0")
        self.__size = size
