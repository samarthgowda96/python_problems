"""102. Binary Tree Level Order Traversal Description
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its level order traversal as:
[
    [3],
    [9,20],
    [15,7]
]"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        queue = [root]

        ans = []
        if not root:
            return ans
        while queue:
            children = []
            size = len(queue)
            for i in range(size):
                root = queue.pop(0)  # visit first item in queue
                children.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(children)
        return ans


"""Submission
Runtime: 32 ms, faster than 74.77% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal."""
