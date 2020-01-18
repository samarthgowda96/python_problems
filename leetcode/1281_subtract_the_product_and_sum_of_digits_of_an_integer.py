'''1281. Subtract the Product and Sum of Digits of an Integer Description
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

Constraints:
1 <= n <= 10^5
'''

import numpy


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        product = numpy.prod(digits)
        return product - sum(digits)


'''Submissions
Runtime: 96 ms, faster than 6.62% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 28.2 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
'''
