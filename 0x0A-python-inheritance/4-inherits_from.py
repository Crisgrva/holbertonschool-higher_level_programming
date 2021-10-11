#!/usr/bin/python3
"""
4. Only sub class of
"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object
    is an instance of a class that inherited (directly
    or indirectly) from the specified class ; otherwise
    False.
    """
    return(issubclass(a_class, obj))
