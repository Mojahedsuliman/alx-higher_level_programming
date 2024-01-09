#!/usr/bin/python3
"""Defines  JSON representation of an object (string)"""
import json


def load_from_json_file(filename):
        """JSON representation"""
        with open(filename) as f:
            return (json.load(f))
