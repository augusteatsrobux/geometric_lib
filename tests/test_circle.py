import math
import unittest

import circle

class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(circle.area(2), math.pi * 4)
        
    def test_perimeter_positive(self):
        self.assertEqual(circle.perimeter(2), math.pi * 4)
    
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)
    
    def test_perimeter_zero(self):
        self.assertEqual(circle.area(0), 0)

if __name__ == '__main__':
    unittest.main()
