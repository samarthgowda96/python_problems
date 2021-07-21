"""21. Merge Two Sorted Lists Description

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        root = ListNode(0)
        current = root

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next

            current = current.next

        if not l1:
            current.next = l2
        else:
            current.next = l1
        return root.next


"""Submission
Runtime: 40 ms, faster than 17.56% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists."""
