#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1, 3.3, 4, -2.2]), 4)

    def test_identical_elements(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
