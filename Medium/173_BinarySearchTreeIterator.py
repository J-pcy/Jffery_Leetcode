"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    """
    def __init__(self, root):
        #:type root: TreeNode
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        #:rtype: bool
        return len(self.stack) > 0

    def next(self):
        #:rtype: int
        node = self.stack[-1]
        res = node
        if not node.right:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right == node:
                node = self.stack.pop()
        else:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return res.val
    """
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    
    def hasNext(self):
        return len(self.stack) > 0
    
    def next(self):
        node = self.stack.pop()
        res = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())