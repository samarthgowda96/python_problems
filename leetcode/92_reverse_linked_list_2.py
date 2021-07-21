"""92. Reverse Linked List II Description
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # get first section of linked list
        counter = 1
        first = ListNode(0)  # stores section before m
        copy_first = first
        while counter != m:
            counter += 1
            first.next = ListNode(head.val)
            head = head.next
            first = first.next

        # perform swap
        prev = None
        for i in range(n - m + 1):
            ans_next = head.next
            head.next = prev
            prev = head
            head = ans_next
        head = prev

        first.next = head
        final = copy_first.next
        while first.next:
            first = first.next
        first.next = ans_next

        return final


"""Submission
Runtime: 24 ms, faster than 92.07% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II."""
