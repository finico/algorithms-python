import unittest
from unittest.mock import Mock, call

from src.breadth_first_search import breadth_first_search


class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.fixture = {
            "first": ["second", "third"],
            "second": ["third", "fourth", "sixth"],
            "third": ["first", "fifth"],
            "fourth": ["eighth"],
            "fifth": ["second", "seventh"]
        }

    def test_empty(self):
        self.assertEqual(
            breadth_first_search(
                {},
                "first",
                lambda x: x == "second"
            ),
            False
        )

    def test_find(self):
        self.assertEqual(
            breadth_first_search(
                self.fixture,
                "first",
                lambda x: x == "seventh"
            ),
            True
        )

    def test_not_find(self):
        self.assertEqual(
            breadth_first_search(
                self.fixture,
                "fourth",
                lambda x: x == "fifth"
            ),
            False
        )

    def test_not_find_when_absent(self):
        self.assertEqual(
            breadth_first_search(
                self.fixture,
                "first",
                lambda x: x == "no"
            ),
            False
        )

    def test_is_bread_first(self):
        spy = Mock(wraps=lambda x: x == "eighth")
        result = breadth_first_search(self.fixture, "first", spy)

        self.assertEqual(result, True)
        self.assertEqual(spy.mock_calls, [
            call("second"),
            call("third"),
            call("fourth"),
            call("sixth"),
            call("first"),
            call("fifth"),
            call("eighth")
        ])
