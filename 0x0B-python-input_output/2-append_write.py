#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends at the end of a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
