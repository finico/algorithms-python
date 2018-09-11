import unittest

from src.breadth_first_search import breadth_first_search


class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.fixture = {
            "test": ["test1", "test2"],
            "test1": ["test2", "test3", "found"],
            "test2": ["test4"],
            "test3": [],
            "test4": [],
            "found": []
        }

    def test_empty(self):
        self.assertEqual(
            breadth_first_search(
                {},
                "test",
                lambda x: x == "found"
            ),
            False
        )

    def test_find(self):
        self.assertEqual(
            breadth_first_search(
                self.fixture,
                "test",
                lambda x: x == "found"
            ),
            True
        )

    def test_not_find(self):
        self.assertEqual(
            breadth_first_search(
                self.fixture,
                "test2",
                lambda x: x == "found"
            ),
            False
        )

    def test_not_find_when_absent(self):
        self.assertEqual(
            breadth_first_search(
                self.fixture,
                "test",
                lambda x: x == "no"
            ),
            False
        )
