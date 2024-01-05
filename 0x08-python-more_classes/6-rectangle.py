#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
        width: The width of the new rectangle
        height: The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Representation of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        re = []
        for i in range(self.__height):
            [re.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                re.append("\n")
        return ("".join(re))

    def __repr__(self):
        """Return the Rectangle representation"""
        re = "Rectangle(" + str(self.__width)
        re += ", " + str(self.__height) + ")"
        return (re)

    def __del__(self):
        """Print deletion message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
