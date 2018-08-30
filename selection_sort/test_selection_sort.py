from unittest import TestCase

from big_o import big_o, complexities, datagen

from selection_sort import selection_sort


class TestSelectionSort(TestCase):
    def test_sort(self):
        self.assertEqual(selection_sort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])

    def test_complexity(self):
        best, _ = big_o(
            selection_sort,
            lambda x: datagen.integers(x // 100, 0, x),
            n_repeats=100
        )
        self.assertIsInstance(best, complexities.Quadratic)
