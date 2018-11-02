"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        if not root:
            return 0
        self.res = 0
        self.helper(root)
        return self.res
    def helper(self, node):
        if not node.left and not node.right:
            self.res += 1
            return True
        if not node.left:
            if self.helper(node.right) and node.val == node.right.val:
                self.res += 1
                return True
        if not node.right:
            if self.helper(node.left) and node.val == node.left.val:
                self.res += 1
                return True
        if node.left and node.right:
            t1 = self.helper(node.left)
            t2 = self.helper(node.right)
            if t1 and t2 and node.val == node.left.val and node.val == node.right.val:
                self.res += 1
                return True
        return False
        """
        self.res = 0
        self.helper(root, -1)
        return self.res
    def helper(self, node, val):
        if not node:
            return True
        t1 = self.helper(node.left, node.val)
        t2 = self.helper(node.right, node.val)
        if not t1 or not t2:
            return False
        self.res += 1
        return node.val == val
        