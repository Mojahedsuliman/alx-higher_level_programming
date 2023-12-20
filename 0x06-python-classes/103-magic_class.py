#!/usr/bin/python3

"""
This module defines the MagicClass that performs calculations on a circle.
"""

import math

class MagicClass:
    """
    Represents a class for circle calculations.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the circle (default is 0).
                                  Must be a number.
        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

