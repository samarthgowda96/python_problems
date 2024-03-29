"""344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."""


class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()


"""Submission
Runtime: 196 ms. Your runtime beats 78.47 % of python3 submissions.
Memory Usage: 18.6 MB. Your memory usage beats 60.83 % of python3 submissions."""
