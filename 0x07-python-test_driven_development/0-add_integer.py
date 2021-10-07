#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """
    Write a function that adds 2 integers.
    """

    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (a + b)
