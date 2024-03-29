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

    @classmethod
    def save_to_file(cls, list_objs):
        """---"""
        filename = cls.__name__ + ".json"
        obj_list = [] if list_objs is None else [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(obj_list)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """---"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """---"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """---"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                list_data = cls.from_json_string(json_data)
                instances = [cls.create(**data) for data in list_data]
                return instances
        except FileNotFoundError:
            return []
