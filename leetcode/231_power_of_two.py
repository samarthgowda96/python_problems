"""231. Power of Two Description

Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 != 0:
            return False
        elif n > 1:
            return self.isPowerOfTwo(n / 2)
        else:
            return False


"""Submission
Runtime: 28 ms, faster than 73.68% of Python3 online submissions for Power of Two.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Two."""
