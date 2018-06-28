"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        self.findPaths(root, [], result)
        return result
    
    def findPaths(self, node, path, res):
        path.append(str(node.val))
        if node.left:
            self.findPaths(node.left, path, res)
        if node.right:
            self.findPaths(node.right, path, res)
        if not node.left and not node.right:
            res.append("->".join(path))
        path.pop()
        