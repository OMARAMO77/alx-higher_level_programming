import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        """Test initialization with default values"""
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

        """Test initialization with custom values"""
        square = Square(10, 2, 3, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size(self):
        """Test getting and setting the size attribute"""
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_str(self):
        """Test the string representation of the square"""
        square = Square(5, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_str)

    def test_update(self):
        """Test updating the square with positional arguments"""
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        """Test updating the square with keyword arguments"""
        square.update(size=8, y=5)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        """Test converting the square to a dictionary"""
        square = Square(5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
