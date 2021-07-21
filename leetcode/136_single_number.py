"""136. Single Number Description
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4"""

import collections


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        c = collections.Counter(nums)

        for num in c:
            if c[num] == 1:
                return num


"""Submission:
Runtime: 80ms
Memory usage: 16MB"""
