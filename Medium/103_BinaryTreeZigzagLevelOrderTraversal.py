"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, node, level, res):
        if not node:
            return
        if level == len(res):
            res.append([])
        if level % 2 == 0:
            res[level].append(node.val)
        else:
            res[level].insert(0, node.val)
        self.dfs(node.left, level + 1, res)
        self.dfs(node.right, level + 1, res)
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
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            if len(res) % 2 == 0:
                tmp.reverse()
                res.append(tmp)
            else:
                res.append(tmp)
        return res
        """
        res = []
        if not root:
            return res
        stack1 = [root]
        stack2 = []
        while stack1 or stack2:
            tmp1 = []
            while stack1:
                node = stack1.pop()
                tmp1.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if tmp1:
                res.append(tmp1)
            tmp2 = []
            while stack2:
                node = stack2.pop()
                tmp2.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            if tmp2:
                res.append(tmp2)
        return res
        