import unittest
from random import randint

from big_o import big_o, complexities

from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_find(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 3), 1)

    def test_not_find(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), None)

    def test_complexity(self):
        best, _ = big_o(
            lambda arr: binary_search(arr, arr[randint(0, len(arr) - 1)]),
            lambda x: list(range(x)),
            n_repeats=1000
        )
        self.assertIsInstance(best, complexities.Logarithmic)
