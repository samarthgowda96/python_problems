'''81. Search in Rotated Sorted Array II Description
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''


class Solution:
    def search(self, nums: [int], target: int) -> bool:
        if target in nums:
            return True
        return False


'''Submission
Runtime: 48 ms, faster than 90.70% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array II.'''
