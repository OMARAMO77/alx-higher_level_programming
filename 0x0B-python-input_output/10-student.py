#!/usr/bin/python3
"""definition of student"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes instance data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a
        Student instance"""
        dictionary = self.__dict__
        if attrs is None:
            return dictionary

        d = {k: v for k, v in dictionary.items() if k in attrs}
        return d
