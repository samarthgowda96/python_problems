"""206. Reverse Linked List Description

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        n = head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        return prev


"""Submission
Runtime: 32 ms, faster than 80.65% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Reverse Linked List."""
