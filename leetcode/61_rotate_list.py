"""61. Rotate List Description
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if k == 0:
            return head
        counter = head
        size = 0
        while counter:
            counter = counter.next
            size += 1
        k = k % size  # this is just in case k includes multiple full rotations

        while k != 0:
            copy = head
            while copy.next.next:
                copy = copy.next
            x = ListNode(copy.next.val)
            copy.next = None
            x.next = head
            head = x
            k -= 1
        return head


"""Submission
Runtime: 48 ms, faster than 14.76% of Python3 online submissions for Rotate List.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Rotate List."""
