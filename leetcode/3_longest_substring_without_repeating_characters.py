"""3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = []
        longest = []
        for letter in s:
            if letter not in curr:
                curr.append(letter)
            else:
                longest.append(len(curr))
                curr = curr[curr.index(letter) + 1 :]
                curr.append(letter)

        longest.append(len(curr))
        return max(longest)


"""Submission
Runtime: 60 ms, faster than 76.53% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB"""
