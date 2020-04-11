'''98. Validate Binary Search Tree Description
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.'''


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # perform inorder traversal using a stack
        result = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        for i in range(len(result) - 1):
            if result[i] < result[i+1]:
                continue
            return False
        return True


'''Submission
Runtime: 40 ms, faster than 84.99% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.1 MB, less than 22.99% of Python3 online submissions for Validate Binary Search Tree.'''
