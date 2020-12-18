# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

class MyTest(unittest.TestCase):

    def test_distance(self):
        #Test distance function.
        v1 = Vector(2.8, -4.7, 0.4)
        v2 = Vector(-8.1, 3.0, -10.6)
        self.assertEqual(v1.distance(v2), 17.294507798720378, "supposed to be 17.294507798720378")

    def test_dot(self):
        v1 = Vector(2.8, -4.7, 0.4)
        v2 = Vector(-8.1, 3.0, -10.6)
        self.assertEqual(v1.dot(v2), -41.02, "supposed to be -41.02")

    def test_cross(self):
        v1 = Vector(2.8, -4.7, 0.4)
        v2 = Vector(-8.1, 3.0, -10.6)
        self.assertIsInstance(v1.cross(v2), Vector)

if __name__ == '__main__':
    unittest.main()
