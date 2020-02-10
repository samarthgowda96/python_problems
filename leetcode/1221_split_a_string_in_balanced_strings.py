'''1221. Split a String in Balanced Strings Description
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R' '''


# solved two different ways
# first solution

import collections


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        substr = []
        ans = 0
        for i in range(len(s)):
            substr.append(s[i])
            c = collections.Counter(substr)
            if c['R'] == c['L']:
                ans += 1
                substr = []
        return ans


'''Submission one
Runtime: 112 ms, faster than 6.08% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.'''


# second solution
class SolutionTwo:
    def balancedStringSplit(self, s: str) -> int:
        right = 0
        left = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == 'R':
                right += 1
            else:
                left += 1
            if right == left:
                ans += 1
        return ans


'''Submission two
Runtime: 24 ms, faster than 88.79% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.'''
