#!/usr/bin/python3
"""Defines a a function that returns
the dictionary description with simple data structure """


def class_to_json(obj):
    """Returns the dictionary description
    with simple data structure"""
    return (obj.__dict__)
