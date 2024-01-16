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
        self.validate_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.validate_positive_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.validate_non_negative_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.validate_non_negative_integer(value, "y")
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
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update attribute and arguments"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

