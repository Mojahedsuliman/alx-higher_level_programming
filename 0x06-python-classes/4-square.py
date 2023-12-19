#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """the square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square side.
        """
        self.size = size

    @property
    def size(self):

        return (self.__size)
    
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size) ** 2
