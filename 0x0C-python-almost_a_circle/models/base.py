#!/usr/bin/python3
"""
1. Base class
"""


import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file
        """
        dicts = []
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
            dicts = Base.to_json_string(dicts)
        else:
            dicts = str(dicts)

        with open("{}.json".format(cls.__name__), mode="w",
                  encoding="utf-8") as f:
            f.write(dicts)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string
        representation json_string
        """
        if not json_string:
            return []
        elif json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load from JSON
        """
        lists = []
        try:
            with open("{}.json".format(cls.__name__),
                      "r", encoding="utf-8") as f:
                dicts = cls.from_json_string(f.read())
                for item in dicts:
                    lists.append(cls.create(**item))
                return lists
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save instances to CSV
        """
        pass

    @classmethod
    def load_from_file_csv(cls):
        """
        Load from CSV
        """
        lists = []
        try:
            with open("{}.csv".format(cls.__name__),
                      "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                items = list(reader)
            for item in items:
                lists.append(cls.create(**item))
            return lists
        except FileNotFoundError:
            return []
