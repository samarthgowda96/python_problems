"""387. First Unique Character in a String Description
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters."""


import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        for letter in sorted(set(s), key=s.index):
            if c[letter] == 1:
                return s.index(letter)
        return -1


"""Submission
Runtime: 72 ms, faster than 92.22% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String."""
