"""941. Valid Mountain Array
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
- A.length >= 3
- There exists some i with 0 < i < A.length - 1 such that:
    - A[0] < A[1] < ... A[i-1] < A[i]
    - A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000"""


class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3:
            return False
        dec = False

        # check that the array starts by increasing
        if A[0] > A[1]:
            return False

        for i in range(len(A) - 1):
            # not strictly increasing
            if A[i] == A[i + 1]:
                return False
            # initialize inc bool to be True
            elif A[i] < A[i + 1] and dec:
                return False
            # if the array starts decreasing
            elif A[i] > A[i + 1]:
                dec = True
            # if the array has already decreased, it shouldn't increase again
            elif dec and A[i] < A[i + 1]:
                return False

        if not dec:
            return False
        return True


"""Submission
Runtime: 432 ms
Memory: 15 MB"""


class Solution2:
    def validMountainArray(self, A: [int]) -> bool:
        n = len(A)
        i = 0

        # walk up
        while i + 1 < n and A[i] < A[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # walk down
        while i + 1 < n and A[i] > A[i + 1]:
            i += 1

        return i == n - 1


"""Submission
Runtime: 212 ms, faster than 92.76% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.1 MB, less than 10.80% of Python3 online submissions for Valid Mountain Array."""
