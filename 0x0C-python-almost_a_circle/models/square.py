#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherts from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

