"""697. Degree of an Array Description
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999."""


import collections


class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        c = collections.Counter(nums)
        max_count = c.most_common()[0][1]
        degree_nums = []
        for number, count in c.most_common():
            if count == max_count:
                degree_nums.append(number)
            else:
                continue

        answers = []
        for num in degree_nums:
            first = nums.index(num)
            last = len(nums) - nums[::-1].index(num) - 1
            answers.append(last - first + 1)
        return min(answers)


"""Submission
Runtime: 1056 ms, faster than 9.36% of Python3 online submissions for Degree of an Array.
Memory Usage: 13.9 MB, less than 81.82% of Python3 online submissions for Degree of an Array."""
