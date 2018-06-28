"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        """
        self.leveldict = {}
        res = []
        self.dfs(root, 1)
        for value in self.leveldict.values():
            res.append(sum(value) / len(value))
        return res
    
    def dfs(self, node, level):
        if not node:
            return
        if level not in self.leveldict:
            self.leveldict[level] = [node.val]
        else:
            self.leveldict[level].append(node.val)
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)
        """
        res = []
        que = []
        que.append(root)
        while que:
            sumlvl = 0
            length = len(que)
            for i in range(length):
                node = que.pop(0)
                sumlvl += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(sumlvl / length)
        return res
        