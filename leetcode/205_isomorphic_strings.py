'''205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        for i in range(len(s)):
            if s[i] not in mappings and t[i] not in list(mappings.values()):
                mappings[s[i]] = t[i]
            elif s[i] not in mappings and t[i] in list(mappings.values()):
                return False
            else:
                if mappings[s[i]] != t[i]:
                    return False
                if list(mappings.values()).count(t[i]) < 1:
                    return False
        return True


'''Submission
Runtime: 212 ms, faster than 5.53% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14 MB, less than 51.46% of Python3 online submissions for Isomorphic Strings.'''
