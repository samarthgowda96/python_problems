"""7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1"""


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        sign = "+"
        if x[0] == "-":
            sign = "-"
            x = x[1:]

        x = int(sign + x[::-1])

        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return 0

        return x


"""Submission
Runtime: 24 ms. Your runtime beats 97.45 % of python3 submissions
Memory Usage: 14.1 MB. Your memory usage beats 73.06 % of python3 submissions"""
