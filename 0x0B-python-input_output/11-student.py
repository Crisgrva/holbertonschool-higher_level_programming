#!/usr/bin/python3
"""
11. Student to disk and reload
"""


class Student:
    """
    Write a class Student that defines a
    student by: (based on 10-student.py)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return(self.__dict__)

        return({item: self.__dict__[item] for item
                in attrs if item in self.__dict__})

    def reload_from_json(self, json):
        try:
            self.first_name = json.get("first_name")
            self.last_name = json.get("last_name")
            self.age = json.get("age")
        except Exception:
            pass
