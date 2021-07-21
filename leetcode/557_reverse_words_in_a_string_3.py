"""557. Reverse Words in a String III Description
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        print(split)
        final = []
        for word in split:
            final.append(word[::-1])

        return " ".join(final)


"""Submission
Runtime: 32 ms, faster than 67.79% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 13.2 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.
"""
