"""86. Partition List Description
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = ListNode(-1)
        first = less  # keep track of head node of less
        more = ListNode(-1)
        second = more  # keep track of head node of more

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                more.next = ListNode(head.val)
                more = more.next
            head = head.next

        copy = less
        while copy.next:
            copy = copy.next
        copy.next = second.next
        return first.next


"""Submission
Runtime: 36 ms, faster than 38.36% of Python3 online submissions for Partition List.
Memory Usage: 13 MB, less than 85.00% of Python3 online submissions for Partition List."""
