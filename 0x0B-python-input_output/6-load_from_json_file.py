#!/usr/bin/python3
"""load_from_json_file funtion"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a 'JSON file'
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
