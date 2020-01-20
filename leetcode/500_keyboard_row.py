'''500. Keyboard Row Description

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.'''


class Solution:
    def findWords(self, words: [str]) -> [str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []

        for word in words:
            current_row = [row for row in rows if word[0].lower() in row]
            if len([letter for letter in word if letter.lower() not in current_row[0]]) == 0:
                result.append(word)

        return result


'''Submission
Runtime: 28 ms, faster than 57.00% of Python3 online submissions for Keyboard Row.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Keyboard Row.'''
