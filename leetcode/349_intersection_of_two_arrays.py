"""349. Intersection of Two Arrays Description

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order."""


class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        intersection = []
        for number in nums1:
            if number in nums2:
                intersection.append(number)

        return intersection


"""Submission
Runtime: 44 ms, faster than 72.07% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays."""
