#!/usr/bin/python3

"""
Define a class Square that represents a square.
"""

class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int or float): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int or float): The size value to set.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if the areas of two squares are equal.

        Args:
            other (Square): Another Square instance to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if the areas of two squares are not equal.

        Args:
            other (Square): Another Square instance to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Check if the area of one square is greater than the other.

        Args:
            other (Square): Another Square instance to compare.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if the area of one square is greater than or equal to the other.

        Args:
            other (Square): Another Square instance to compare.

        Returns:
            bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Check if the area of one square is less than the other.

        Args:
            other (Square): Another Square instance to compare.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if the area of one square is less than or equal to the other.

        Args:
            other (Square): Another Square instance to compare.

        Returns:
            bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

