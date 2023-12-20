#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """the square."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """the square value now"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the return value for square"""
        return self.__size ** 2
    def my_print(self):

        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
