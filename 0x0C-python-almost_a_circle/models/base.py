#!/usr/bin/python3
"""
1. Base class
"""


import json


class Base:
    """
    This class will be the “base” of all other classes
    in this project. The goal of it is to manage
    attribute in all your future classes and to avoid
    duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation
        of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        elif list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
