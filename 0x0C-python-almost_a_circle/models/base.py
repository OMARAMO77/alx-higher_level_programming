#!/usr/bin/python3
"""the class Base"""
import json


class Base:
    """
    Defining the class Base

    Attributes:
        nb_objects (int): Private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes class and object data

        Args:
            id (int): an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """---"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
