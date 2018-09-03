import unittest

from src.recursive_sum import recursive_sum


class TestRecursiveSum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(recursive_sum([]), 0)

    def test_sum(self):
        self.assertEqual(recursive_sum([1, 22, 333]), 356)
