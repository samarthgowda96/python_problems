'''859. Buddy Strings Description
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false

Note:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.'''


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B:
            count = {}
            for s in A:
                if s in count:
                    count[s] += 1
                else:
                    count[s] = 1
            for key in count:
                if count[key] >= 2:
                    return True
            return False
        elif len(A) != len(B):
            return False
        diff_a = []
        diff_b = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_a.append(A[i])
                diff_b.append(B[i])
        if len(diff_a) != 2 or len(diff_b) != 2:
            return False
        if sorted(diff_a) == sorted(diff_b):
            return True
        return False


'''Submission
Runtime: 32 ms, faster than 61.14% of Python3 online submissions for Buddy Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Buddy Strings.'''
