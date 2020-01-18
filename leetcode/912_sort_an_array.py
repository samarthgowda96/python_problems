'''912. Sort an Array Description
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''


class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        return sorted(nums)


'''Submission
Runtime: 132 ms, faster than 96.97% of Python3 online submissions for Sort an Array.
Memory Usage: 19.1 MB, less than 100.00% of Python3 online submissions for Sort an Array.'''
