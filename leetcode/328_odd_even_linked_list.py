"""328. Odd Even Linked List Description
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ..."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(-1)
        final1 = odd
        even = ListNode(-1)
        final2 = even

        counter = 1
        while head:
            if counter % 2 == 1:
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next
            counter += 1
            head = head.next

        odd.next = final2.next
        return final1.next


"""Submission
Runtime: 52 ms, faster than 16.93% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 15.4 MB, less than 8.33% of Python3 online submissions for Odd Even Linked List."""
