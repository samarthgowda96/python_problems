'''260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?'''


from collections import Counter


class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        c = Counter()
        c.update(nums)
        ans = []
        for num in c:
            if c[num] == 1:
                ans.append(num)
            if len(ans) == 2:
                return ans


'''Submission
Runtime: 64 ms, faster than 62.45% of Python3 online submissions for Single Number III.
Memory Usage: 15.5 MB, less than 19.30% of Python3 online submissions for Single Number III.'''
