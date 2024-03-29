"""896. Monotonic Array Description
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true

Note:
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""

from collections import OrderedDict


class Solution:
    def isMonotonic(self, A: [int]) -> bool:
        unique = list(OrderedDict.fromkeys(A))

        if len(unique) == 1:
            return True
        elif unique[0] < unique[1]:
            increasing = True
        else:
            increasing = False

        monotone = True
        for i in range(len(A) - 1):
            if increasing:
                monotone = monotone and A[i] <= A[i + 1]
            else:
                monotone = monotone and A[i] >= A[i + 1]

        return monotone


"""Submissions
Runtime: 524 ms, faster than 54.26% of Python3 online submissions for Monotonic Array.
Memory Usage: 18.7 MB, less than 5.26% of Python3 online submissions for Monotonic Array.
"""
