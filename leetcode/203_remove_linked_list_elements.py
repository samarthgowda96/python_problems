"""203. Remove Linked List Elements Description
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        iterate = ListNode(-1)
        iterate.next = head
        final = iterate
        while iterate.next is not None:
            if iterate.next.val == val:
                iterate.next = iterate.next.next
            else:
                iterate = iterate.next
        return final.next


"""Submission
Runtime: 52 ms, faster than 99.76% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements."""
