"""445. Add Two Numbers II Description
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        a = l1
        b = l2
        one = []
        two = []

        while a:
            one.append(a.val)
            a = a.next
        while b:
            two.append(b.val)
            b = b.next

        first = int("".join(map(str, one)))
        second = int("".join(map(str, two)))

        final = first + second
        final = [int(d) for d in str(final)]

        ans = ListNode(-1)
        submit = ans

        for i in range(len(final)):
            ans.next = ListNode(final[i])
            ans = ans.next

        return submit.next


"""Submission
Runtime: 80 ms, faster than 26.67% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II."""
