"""283. Move Zeroes Description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations."""


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for num in nums:
            if num == 0:
                counter += 1

        for count in range(counter):
            nums.pop(nums.index(0))
            nums.append(0)
        return nums


"""Submission
Runtime: 120 ms
Memory Usage: 15.2 MB"""
