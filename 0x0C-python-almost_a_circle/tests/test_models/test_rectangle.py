import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        """Test initialization with default values"""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertIsNotNone(rectangle.id)

        """Test initialization with custom values"""
        rectangle = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

if __name__ == '__main__':
    unittest.main()
