'''844. Backspace String Compare Description
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        clean_s = ''
        clean_t = ''
        for letter in S:
            if letter != "#":
                clean_s += letter
            else:
                clean_s = clean_s[:-1]
        for letter in T:
            if letter != "#":
                clean_t += letter
            else:
                clean_t = clean_t[:-1]
        return clean_s == clean_t


'''Submission
Runtime: 28 ms, faster than 70.48% of Python3 online submissions for Backspace String Compare.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.'''
