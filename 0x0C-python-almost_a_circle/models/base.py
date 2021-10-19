#!/usr/bin/python3
"""
1. Base class
"""


class Base:
    """
    This class will be the “base” of all other classes
    in this project. The goal of it is to manage
    attribute in all your future classes and to avoid
    duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        if not isinstance(id, None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
