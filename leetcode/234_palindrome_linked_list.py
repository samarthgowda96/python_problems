"""234. Palindrome Linked List Description
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        palindrome = []
        while head:
            palindrome.append(head.val)
            head = head.next
        return palindrome == palindrome[::-1]


"""Submission
Runtime: 72 ms, faster than 55.13% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 22.9 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List."""
