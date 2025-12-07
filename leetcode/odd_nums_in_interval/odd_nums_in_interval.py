"""
7 Dec 2025 Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""


def count_odds(low: int, high: int) -> int:
    diff = high - low
    low_even = low % 2 == 0
    diff_even = diff % 2 == 0
    if low_even and diff_even:
        return diff // 2
    else:
        return diff // 2 + 1
