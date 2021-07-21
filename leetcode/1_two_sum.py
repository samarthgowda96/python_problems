"""1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""


class Solution:
    def twoSum(self, nums, target):
        answer = []
        for x in range(len(nums)):
            y = target - nums[x]
            if y in nums and nums.index(y) != x:
                answer.append(x)
                answer.append(nums.index(y))
                answer.sort()
                return answer


"""Submission
Runtime: 1176 ms, faster than 24.17% of Python3 online submissions for Two Sum.
Memory Usage: 14.7 MB, less than 98.69% of Python3 online submissions for Two Sum."""
