"""520. Detect Capital Description

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters."""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower():
            return True
        if word == word.upper():
            return True
        if word == word[0].upper() + word[1::].lower():
            return True
        return False


"""Submission
Runtime: 28 ms, faster than 68.14% of Python3 online submissions for Detect Capital.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Detect Capital."""
