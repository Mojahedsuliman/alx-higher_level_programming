#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """the square"""

    def __init__(self, size=0):
        """Initializes the square
        Args:
        size (int): The size of square
        TypeError: if size doesn't integer
        ValueError: if the size is < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
