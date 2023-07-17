import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    def test_attributes(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_setters(self):
        r4 = Rectangle(5, 5)
        r4.width = 15
        r4.height = 20
        r4.x = 3
        r4.y = 4

        self.assertEqual(r4.width, 15)
        self.assertEqual(r4.height, 20)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
