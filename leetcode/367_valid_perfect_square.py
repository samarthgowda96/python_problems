'''367. Valid Perfect Square Description

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num > 0:
            return int(num**(0.5)) == num**(0.5)
        return False


'''Submission
Runtime: 32 ms, faster than 30.99% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Valid Perfect Square.'''
