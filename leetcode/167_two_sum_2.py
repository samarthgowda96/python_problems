"""167. Two Sum II - Input array is sorted Description

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.


Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2."""


class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        for number in list(set(numbers)):
            if (target - number) in numbers:
                if number == target - number:
                    return sorted(
                        [numbers.index(number) + 1, numbers.index(number) + 2]
                    )
                else:
                    return sorted(
                        [numbers.index(number) + 1, numbers.index(target - number) + 1]
                    )


"""Submission
Runtime: 60 ms, faster than 88.39% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted."""
