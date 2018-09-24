"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        res = []
        self.postorder(root, res)
        return res
    
    def postorder(self, root, res):
        if not root:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
        """
        """
        if not root:
            return []
        res = []
        stack = [root]
        node = root
        while stack:
            tmp = stack[-1]
            if (not tmp.left and not tmp.right) or tmp.left == node or tmp.right == node:
                res.append(stack.pop().val)
                node = tmp
            else:
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
        return res
        """
        """
        res = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                res.insert(0, node.val)
                node = node.right
            else:
                tmp = stack.pop()
                node = tmp.left
        return res
        """
        