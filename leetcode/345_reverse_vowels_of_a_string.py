'''345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if not s:
            return ''
        split_string = []
        list_of_vowels = []
        for letter in s:
            if letter in vowels:
                list_of_vowels.append(letter)
                split_string.append(None)
            else:
                split_string.append(letter)

        list_of_vowels = list_of_vowels[::-1]  # reverse the list
        final = ''
        for letter in split_string:
            if letter:
                final += letter
            else:
                final += list_of_vowels[0]
                del list_of_vowels[0]
        return final


'''Submission
Runtime: 256 ms, faster than 5.12% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15.4 MB, less than 30.05% of Python3 online submissions for Reverse Vowels of a String.'''
