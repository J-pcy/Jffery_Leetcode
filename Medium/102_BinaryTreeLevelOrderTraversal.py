"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
        """
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, node, level, res):
        if not node:
            return 
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        if node.left:
            self.dfs(node.left, level + 1, res)
        if node.right:
            self.dfs(node.right, level + 1, res)
        