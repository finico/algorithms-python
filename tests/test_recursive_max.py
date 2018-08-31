import unittest

from src.recursive_max import recursive_max


class TestRecursiveMax(unittest.TestCase):
    def test_when_empty(self):
        self.assertIsNone(recursive_max([]))

    def test_max_pair(self):
        self.assertEqual(recursive_max([5, 2]), 5)

    def test_max(self):
        self.assertEqual(recursive_max([1, 55, 29, 73, 6]), 73)
