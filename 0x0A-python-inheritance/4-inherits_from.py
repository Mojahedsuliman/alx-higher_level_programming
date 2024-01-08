#!/usr/bin/python3
"""Defines a class-checking function"""


def inherits_from(obj, a_class):
    """Check if an object is exatly an instance of a given class
    Args:
        obj: The object to be checked
        a_class: The class to match the type of obj to
        Returns:
        If obj is inheritly or instance of a_class - True
            Otherwise - False
        """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
