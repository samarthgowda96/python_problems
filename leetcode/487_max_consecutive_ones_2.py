"""487. Max Consecutive Ones II
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        longest_seq = 0
        left_idx, right_idx = 0, 0
        zero_count = 0

        while right_idx < len(nums):
            if nums[right_idx] == 0:
                zero_count += 1
            while zero_count == 2:
                if nums[left_idx] == 0:
                    zero_count -= 1
                left_idx += 1

            longest_seq = max(longest_seq, right_idx - left_idx + 1)
            right_idx += 1
        return longest_seq
