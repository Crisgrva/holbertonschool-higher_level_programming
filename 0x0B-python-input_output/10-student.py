#!/usr/bin/python3
"""
9. Student to JSON
"""


class Student:
    """
    Write a class Student that defines a student by:
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
