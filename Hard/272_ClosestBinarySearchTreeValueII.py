"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        """
        res = []
        nodes = []
        self.helper(root, nodes)
        left = len(nodes) - 1
        right = len(nodes)
        for i in range(len(nodes)):
            if nodes[i] > target:
                left = i - 1
                right = i
                break
        for i in range(k):
            if left < 0:
                res.append(nodes[right])
                right += 1
            elif right >= len(nodes):
                res.append(nodes[left])
                left -= 1
            else:
                if abs(nodes[left] - target) < abs(nodes[right] - target):
                    res.append(nodes[left])
                    left -= 1
                else:
                    res.append(nodes[right])
                    right += 1
        return res
        
    def helper(self, root, nodes):
        if not root:
            return
        self.helper(root.left, nodes)
        nodes.append(root.val)
        self.helper(root.right, nodes)
        """
        res = []
        pre, nxt = [], []
        while root:
            if root.val <= target:
                pre.append(root)
                root = root.right
            else:
                nxt.append(root)
                root = root.left
        for i in range(k):
            if not pre:
                res.append(nxt[-1].val)
                self.getNxt(nxt)
            elif not nxt:
                res.append(pre[-1].val)
                self.getPre(pre)
            else:
                if abs(pre[-1].val - target) < abs(nxt[-1].val - target):
                    res.append(pre[-1].val)
                    self.getPre(pre)
                else:
                    res.append(nxt[-1].val)
                    self.getNxt(nxt)
        return res
    
    def getPre(self, pre):
        tmp = pre.pop()
        if tmp.left:
            pre.append(tmp.left)
            while pre[-1].right:
                pre.append(pre[-1].right)
    
    def getNxt(self, nxt):
        tmp = nxt.pop()
        if tmp.right:
            nxt.append(tmp.right)
            while nxt[-1].left:
                nxt.append(nxt[-1].left)
        