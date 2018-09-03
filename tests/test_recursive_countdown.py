from unittest import TestCase
from unittest.mock import patch, call

from src.recursive_countdown import recursive_countdown


class TestRecursiveCountdown(TestCase):
    @patch('builtins.print')
    def test_countdown(self, mocked_print):
        recursive_countdown(3)
        self.assertEqual(len(mocked_print.mock_calls), 4)
        self.assertEqual(mocked_print.call_args_list[0], call(3))
        self.assertEqual(mocked_print.call_args_list[1], call(2))
        self.assertEqual(mocked_print.call_args_list[2], call(1))
        self.assertEqual(mocked_print.call_args_list[3], call(0))
