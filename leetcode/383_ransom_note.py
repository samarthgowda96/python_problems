"""383. Ransom Note Description
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False
        return True


"""Submission
Runtime: 24 ms, faster than 99.93% of Python3 online submissions for Ransom Note.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Ransom Note."""
