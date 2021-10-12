#!/usr/bin/python3
"""
12. My integer
"""


class MyInt(int):
    """
    Write a class MyList that inherits from list
    """

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.__dict__ == value.__dict__
        else:
            return False

    def __ne__(self, value):
        return not self.__eq__(value)
