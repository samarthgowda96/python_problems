'''88. Merge Sorted Array Description
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
- The number of elements initialized in nums1 and nums2 are m and n respectively.
- You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


'''Submission
Runtime: 48 ms, faster than 28.49% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
'''


class Solution2:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sort = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                sort.append(nums1[i])
                i += 1
            else:
                sort.append(nums2[j])
                j += 1
        if i < m:
            while i < m:
                sort.append(nums1[i])
                i += 1
        if j < n:
            while j < n:
                sort.append(nums2[j])
                j += 1
        for i in range(len(nums1)):
            nums1[i] = sort[i]


'''Submission
Runtime: 44 ms, faster than 42.21% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.6 MB, less than 94.57% of Python3 online submissions for Merge Sorted Array.'''
