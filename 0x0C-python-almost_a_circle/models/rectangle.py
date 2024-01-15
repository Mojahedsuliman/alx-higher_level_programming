#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class,
    inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def validate_positive_integer(self, value, attribute_name):
        """Validate if the value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative_integer(self, value, attribute_name):
        """Validate if the value is a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def area(self):
        """Return area"""
        return (self.width * self.height)

    def display(self):
        """Display the Rectangle instance with #"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
            return

    def __str__(self):
        """Return a str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height))
