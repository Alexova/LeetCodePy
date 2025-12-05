import unittest

from leetcode.partitions.partitions_with_even_sum_difference import count_partitions

class TestPartitionsWithEvenSumDifference(unittest.TestCase):

    def test_empty_list(self):
        assert count_partitions([]) == 0


    def test_odd_total_sum(self):
        assert count_partitions([10, 10, 3, 7, 6]) == 4


    def test_even_total_sum_longer(self):
        assert count_partitions([1, 2, 2]) == 0


    def test_all_even_numbers(self):
        assert count_partitions([2, 4, 6, 8]) == 3
