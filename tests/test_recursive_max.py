import unittest

from src.recursive_max import recursive_max


class TestRecursiveMax(unittest.TestCase):
    def test_when_empty(self):
        self.assertRaises(AssertionError, recursive_max, [])

    def test_max(self):
        self.assertEqual(recursive_max([1, 55, 29, 73, 6]), 73)

    def test_max_one(self):
        self.assertEqual(recursive_max([5]), 5)
