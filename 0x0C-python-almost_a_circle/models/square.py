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

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
