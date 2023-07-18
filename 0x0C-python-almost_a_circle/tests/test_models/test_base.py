import unittest
import json
from base import Base


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        """Test when list_dictionaries is None"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

        """Test when list_dictionaries is an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        """Test when list_dictionaries contains data"""
        list_dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expected_json = json.dumps(list_dictionaries)
        result = Base.to_json_string(list_dictionaries)
        self.assertEqual(result, expected_json)

    def test_save_to_file(self):
        """Test when list_objs is None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            result = file.read()
        self.assertEqual(result, "[]")

        """Test when list_objs is an empty list"""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            result = file.read()
        self.assertEqual(result, "[]")

        """Test when list_objs contains objects"""
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        with open("Base.json", "r") as file:
            result = file.read()
        expected_json = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()
