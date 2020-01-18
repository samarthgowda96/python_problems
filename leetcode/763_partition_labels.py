'''763. Partition Labels Description
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''


class Solution:
    def partitionLabels(self, S: str) -> [int]:
        partition = []
        while S:
            first_idx = 0
            last_idx = S.rfind(S[first_idx])
            updated_last_idx = find_index(S, first_idx, last_idx)
            if last_idx != updated_last_idx:
                last_idx = updated_last_idx
                updated_last_idx = find_index(S, first_idx, last_idx)
            while last_idx != updated_last_idx:
                last_idx = updated_last_idx
                updated_last_idx = find_index(S, first_idx, last_idx)

            partition.append(updated_last_idx+1)
            S = S[updated_last_idx+1:]
        return partition


def find_index(string, first, last_idx):
    for letter in list(set(string[0:last_idx+1])):
        if string.rfind(letter) > last_idx:
            last_idx = string.rfind(letter)
    return last_idx


'''Submission
Runtime: 36 ms, faster than 77.67% of Python3 online submissions for Partition Labels.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Partition Labels.'''
