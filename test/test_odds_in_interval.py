import unittest
from leetcode.odd_nums_in_interval.odd_nums_in_interval import count_odds

class TestCountOddsInTheInterval(unittest.TestCase):

    def test_start_even_diff_even(self):
        assert count_odds(2, 8) == 3

    def test_start_uneven_diff_even(self):
        assert count_odds(3, 9) == 4

    def test_start_uneven_diff_uneven(self):
        assert count_odds(3, 10) == 4

    def test_start_even_diff_uneven(self):
        assert count_odds(2, 9) == 4
