#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return (self.__dict__)
