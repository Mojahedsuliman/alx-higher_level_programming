#!/usr/bin/python3
"""Defines the JSON representation of an object (string)"""
import json


def save_to_json_file(my_obj, filename):
    """JSON representation"""
    with open(filename, 'w') as f:
        return (json.dump(my_obj, f))
