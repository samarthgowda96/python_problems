"""232. Implement Queue using Stacks Description

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue)."""


from collections import deque


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        new_stack = deque()
        for i in range(len(self.stack)):
            new_stack.append(self.stack.pop())
        ans = new_stack.pop()
        for i in range(len(new_stack)):
            self.stack.append(new_stack.pop())
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        new_stack = deque()
        for i in range(len(self.stack)):
            new_stack.append(self.stack.pop())
        ans = new_stack.pop()
        self.stack.append(ans)
        for i in range(len(new_stack)):
            self.stack.append(new_stack.pop())
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""Submission
Runtime: 16 ms, faster than 99.68% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks."""
