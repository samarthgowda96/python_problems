"""509. Fibonacci Number Description

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30."""


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)


"""Submission
Runtime: 876 ms, faster than 22.12% of Python3 online submissions for Fibonacci Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Fibonacci Number."""
