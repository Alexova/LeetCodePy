from typing import List

"""
You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even.
"""

def count_partitions(nums: List[int]) -> int:
    sum_total = 0
    count = 0
    for i in range(len(nums)):
        sum_total += nums[i]
    if sum_total % 2 == 1:
        return 0
    sum_partition_1 = 0
    for i in range(len(nums) - 1):
        sum_partition_1 += nums[i]
        if sum_partition_1 % 2 == (sum_total - sum_partition_1) % 2:
            print(
                "i=", i,
                "; tempSum=", sum_partition_1,
                "; tempSum2=", (sum_total - sum_partition_1)
            )
            count += 1
    return count

