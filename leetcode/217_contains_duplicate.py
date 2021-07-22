"""217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109"""


from collections import Counter


class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        c = Counter(nums)
        for key in c:
            if c[key] > 1:
                return True
        return False


"""Submission
Runtime: 112 ms, faster than 92.58% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21.6 MB"""
