'''53. Maximum Subarray Description
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.'''


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if not nums:
            return -2147483648
        abs_max = nums[0]
        local_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i] + local_max:
                local_max = nums[i] + local_max
            else:
                local_max = nums[i]
            if abs_max < local_max:
                abs_max = local_max

        return abs_max


'''Submission
Runtime: 68 ms
Memory Usage: 14.6 MB'''
