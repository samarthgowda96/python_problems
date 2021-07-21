"""1089. Duplicate Zeros
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9"""


class Solution:
    def duplicateZeros(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []
        for num in arr:
            if num != 0:
                new_arr.append(num)
            else:
                new_arr.append(0)
                new_arr.append(0)
        for i in range(len(arr)):
            arr[i] = new_arr[i]


"""Submission
Runtime: 72 ms, faster than 76.90% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 14.5 MB, less than 34.08% of Python3 online submissions for Duplicate Zeros."""
