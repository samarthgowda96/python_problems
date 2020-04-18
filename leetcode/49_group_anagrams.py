'''49. Group Anagrams Description
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.'''


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        words = {}
        for word in strs:
            if str(sorted(word)) in words:
                words[str(sorted(word))].append(word)
            else:
                words[str(sorted(word))] = [word]
        return words.values()


'''Submission
Runtime: 116 ms, faster than 54.79 of Python3 online submissions for Group Anagrams.
Memory Usage: 17.5 MB, less than 30.19% of Python3 online submissions for Group Anagrams.'''
