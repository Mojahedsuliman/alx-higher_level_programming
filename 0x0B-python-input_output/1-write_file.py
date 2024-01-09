#!/usr/bin/python3
"""Defines a function that writes a string using with"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF-8)"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
