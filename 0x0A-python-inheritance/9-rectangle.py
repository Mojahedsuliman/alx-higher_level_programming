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
        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            """Return the Rectangle area"""
            return (self.__width * self.__height)

            def __str__(self):
                """Return the printable representation of the Rectangle"""
                string = "[" + str(self.__class__.__name__) + "] "
                string += str(self.__width) + "/" + str(self.__height)
                return (string) 
