#!/usr/bin/python3
"""
3. Print square
"""


def print_square(size):
    """
    Write a function that prints a square with the character #.
    """
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("{}".format("#" * size))
