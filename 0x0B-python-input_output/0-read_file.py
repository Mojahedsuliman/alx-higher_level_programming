#!/usr/bin/python3
"""Defines a function that reads a text file using with"""
 

def read_file(filename=""):
    """prints the file content"""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
