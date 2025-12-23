import unittest

import square

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(4), 16)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(5), 20)

if __name__ == '__main__':
    unittest.main()
