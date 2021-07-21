"""20. Valid Parentheses Description
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true"""


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        stack = deque()
        if not s:
            return True
        for letter in s:
            if letter in opening:
                stack.append(letter)
            else:
                closing_idx = closing.index(letter)
                if not stack:
                    return False
                opening_idx = opening.index(stack[-1])
                if closing_idx != opening_idx:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True


"""Submission
Runtime: 28 ms, faster than 71.52% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses."""
