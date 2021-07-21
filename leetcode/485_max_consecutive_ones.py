"""485. Max Consecutive Ones Description

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        counts = []
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counts.append(counter)
                counter = 0
        counts.append(counter)
        return max(counts)


"""Description
Runtime: 388 ms, faster than 50.74% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones."""
