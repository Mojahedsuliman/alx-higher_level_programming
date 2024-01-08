#!/usr/bin/python3
"""Defines a Base Geometry class based in 5-base_geometry.py"""


class BaseGeometry:
    """Represents a BaseGeometry"""

    def area(self):
        """Are not implemented"""

        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate a parameter as an integer
        Args:
            name: The parameter name
            value: The parameter value
            Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
            """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
