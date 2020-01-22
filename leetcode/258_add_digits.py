'''258. Add Digits Description

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?'''


class Solution:
    def addDigits(self, num: int) -> int:
        my_list = [int(x) for x in str(num)]
        while len(my_list) > 1:
            my_list = [int(x) for x in str(num)]
            num = sum(my_list)
        return num


'''Submission
Runtime: 48 ms, faster than 7.30% of Python3 online submissions for Add Digits.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Digits.'''
