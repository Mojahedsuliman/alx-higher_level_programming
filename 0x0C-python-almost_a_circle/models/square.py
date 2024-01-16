#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherts from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes and arguments"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
