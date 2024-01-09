#!/usr/bin/python3
"""Defines a function that returns
the JSON representation of an object (string)"""
import json


def from_json_string(my_str):
    """Returns the JSON representation"""
    return (json.loads(my_str))
