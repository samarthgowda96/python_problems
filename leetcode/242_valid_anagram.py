"""242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count


"""Submission
Runtime: 63 ms. Your runtime beats 23.53 % of python3 submissions.
Memory Usage: 14.5 MB. Your memory usage beats 56.56 % of python3 submissions."""
