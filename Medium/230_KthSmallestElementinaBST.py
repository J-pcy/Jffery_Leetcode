"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        """
        self.num = k
        return self.helper(root)
    
    def helper(self, root):
        if not root:
            return -1
        val = self.helper(root.left)
        if self.num == 0:
            return val
        self.num -= 1
        if self.num == 0:
            return root.val
        return self.helper(root.right)
        """
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack[-1]
            k -= 1
            if k == 0:
                return node.val
            if not node.right:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return -1
        """
        """
        cnt = self.helper(root.left)
        if cnt >= k:
            return self.kthSmallest(root.left, k)
        if cnt + 1 < k:
            return self.kthSmallest(root.right, k - 1 - cnt)
        return root.val
        
    def helper(self, node):
        if not node:
            return 0
        return 1 + self.helper(node.left) + self.helper(node.right)
        """
        nodedict = {}
        self.countNodes(root, nodedict)
        return self.findNode(root, k, nodedict)
    
    def countNodes(self, root, nodedict):
        if not root:
            return 0
        left = self.countNodes(root.left, nodedict)
        right = self.countNodes(root.right, nodedict)
        nodedict[root] = left + right + 1
        return 1 + left + right
    
    def findNode(self, root, k, nodedict):
        if not root:
            return -1
        cnt = 0 if not root.left else nodedict[root.left]
        if cnt >= k:
            return self.findNode(root.left, k, nodedict)
        if cnt < k - 1:
            return self.findNode(root.right, k - 1 - cnt, nodedict)
        return root.val
    