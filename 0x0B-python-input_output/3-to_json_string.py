#!/usr/bin/python3
"""to_json_string function """
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    obj_json = json.dumps(my_obj)
    return obj_json
