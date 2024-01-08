#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Represents a rectangle from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle
        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height")
        self.__height = height
