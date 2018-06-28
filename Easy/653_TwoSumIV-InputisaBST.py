"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        nums_dict = {}
        return self.helper(root, k, nums_dict)
    
    def helper(self, root, k, nums_dict):
        if not root:
            return False
        if k - root.val in nums_dict:
            return True
        nums_dict[root.val] = 1
        return self.helper(root.left, k, nums_dict) or self.helper(root.right, k, nums_dict)
        