import unittest

from big_o import big_o, complexities, datagen

from src.quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_one(self):
        self.assertEqual(quicksort([4]), [4])

    def test_sort(self):
        self.assertEqual(quicksort([3, 2, 5, 1, 4]), [1, 2, 3, 4, 5])

    def test_complexity(self):
        best, _ = big_o(
            quicksort,
            lambda x: datagen.integers(x // 100, 0, x // 100),
            n_repeats=100
        )
        self.assertIsInstance(best, complexities.Linearithmic)  # O(n log n)
