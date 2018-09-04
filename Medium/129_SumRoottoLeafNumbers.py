"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        res = []
        if not root:
            return 0
        self.helper(root, res, root.val)
        return sum(res)
    
    def helper(self, root, res, num):
        if not root.left and not root.right:
            res.append(num)
        if root.left:
            self.helper(root.left, res, 10 * num + root.left.val)
        if root.right:
            self.helper(root.right, res, 10 * num + root.right.val)
        """
        return self.dfs(root, 0)
    
    def dfs(self, node, pathsum):
        if not node:
            return 0
        pathsum = 10 * pathsum + node.val
        if not node.left and not node.right:
            return pathsum
        return self.dfs(node.left, pathsum) + self.dfs(node.right, pathsum)
        