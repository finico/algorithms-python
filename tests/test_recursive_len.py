import unittest

from src.recursive_len import recursive_len


class TestRecursiveLen(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(recursive_len([]), 0)

    def test_len(self):
        self.assertEqual(recursive_len([1, 2, 3, 4, 5]), 5)
