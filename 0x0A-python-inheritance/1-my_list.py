#!/usr/bin/python3
"""Defines an inherited list class"""


class MyList(list):
    """Inherits from list"""
    def __init__(self):
        """Initialize a new list"""
        super().__init__()

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
