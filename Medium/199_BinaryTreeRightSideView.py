"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if i == 0:
                    tmp = node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(tmp)
        return res
        """
        res = []
        tmp = []
        self.dfs(root, 0, tmp)
        for i in range(len(tmp)):
            res.append(tmp[i][0])
        return res
    def dfs(self, node, level, tmp):
        if not node:
            return
        if level == len(tmp):
            tmp.append([])
        tmp[level].append(node.val)
        self.dfs(node.right, level + 1, tmp)
        self.dfs(node.left, level + 1, tmp)
        """
        