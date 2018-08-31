from unittest import TestCase
from unittest.mock import patch

from src.recursive_countdown import recursive_countdown


class TestRecursiveCountdown(TestCase):
    @patch('builtins.print')
    def test_countdown(self, mocked_print):
        recursive_countdown(3)
        self.assertEqual(len(mocked_print.mock_calls), 4)
