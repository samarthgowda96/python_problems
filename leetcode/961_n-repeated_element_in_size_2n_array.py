"""961. N-Repeated Element in Size 2N Array Description

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:
Input: [1,2,3,3]
Output: 3

Example 2:
Input: [2,1,2,5,3,2]
Output: 2

Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even"""


import collections


class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        c = collections.Counter(A)
        for number in c:
            if c[number] > 1:
                return number


"""Submission
Runtime: 236 ms, faster than 31.89% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 14 MB, less than 87.76% of Python3 online submissions for N-Repeated Element in Size 2N Array."""
