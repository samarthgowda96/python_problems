'''977. Squares of a Sorted Array Description
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.'''


class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        final = []
        for number in A:
            final.append(number * number)
        return sorted(final)


'''Submission
Runtime: 228 ms, faster than 81.22% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 14.7 MB, less than 94.05% of Python3 online submissions for Squares of a Sorted Array.'''
