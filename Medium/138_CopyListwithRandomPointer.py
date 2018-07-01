"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        """
        if not head:
            return None
        res = RandomListNode(head.label)
        node  = res
        cur = head.next
        nodedict = {head: res}
        while cur:
            tmp = RandomListNode(cur.label)
            node.next = tmp
            nodedict[cur] = tmp
            node = node.next
            cur = cur.next
        node = res
        cur = head
        while node:
            if cur.random:
                node.random = nodedict[cur.random]
            else:
                node.random = None
            node = node.next
            cur = cur.next
        return res
        """
        """
        def copyNode(node, nodedict):
            if not node: return None
            if node in nodedict: return nodedict[node]
            copy = RandomListNode(node.label)
            nodedict[node] = copy
            copy.next = copyNode(node.next, nodedict)
            copy.random = copyNode(node.random, nodedict)
            return copy
        return copyNode(head, {})
        """
        if not head:
            return None
        newnode = head
        while newnode:
            tmp = RandomListNode(newnode.label)
            tmp.next = newnode.next
            newnode.next = tmp
            newnode = newnode.next.next
        newnode = head
        while newnode:
            if newnode.random:
                newnode.next.random = newnode.random.next
            newnode = newnode.next.next
        newnode = head.next
        pold = head
        pnew = head.next
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newnode
        