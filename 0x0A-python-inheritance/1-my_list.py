#!/usr/bin/python3
"""
1. My list
"""


class MyList(list):
    """
    Write a class MyList that inherits from list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
