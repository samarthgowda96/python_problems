'''14. Longest Common Prefix Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.'''


class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if strs == []:
            return ''
        strs = sorted(strs)
        if len(strs) == 1:
            return strs[0]
        first_word = strs[0]
        last_word = strs[-1]
        if len(first_word) < len(last_word):
            shorter = first_word
            longer = last_word
        else:
            shorter = last_word
            longer = first_word
        final = ''
        for i in range(len(shorter)):
            if shorter[i] == longer[i]:
                final += shorter[i]
            else:
                return final
        return final


'''Submission
Runtime: 32 ms, faster than 66.68% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
'''
