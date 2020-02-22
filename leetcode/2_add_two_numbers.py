'''2. Add Two Numbers Description

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''


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

        l1_vals = []
        n = l1
        while n is not None:
            l1_vals.append(n.val)
            n = n.next

        l2_vals = []
        m = l2
        while m is not None:
            l2_vals.append(m.val)
            m = m.next
        first = l1_vals[::-1]
        second = l2_vals[::-1]
        first = int("".join(map(str, first)))
        second = int("".join(map(str, second)))

        total = first + second
        total = [int(d) for d in str(total)][::-1]
        ans = ListNode(-1)
        final = ans
        for i in range(len(total)):
            ans.next = ListNode(total[i])
            ans = ans.next
        return final.next


'''Submission
Runtime: 76 ms, faster than 30.02% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.'''
