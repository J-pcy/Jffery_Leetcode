"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = ListNode(0)
        part1 = res
        tmp = ListNode(0)
        part2 = tmp
        while head:
            if head.val < x:
                part1.next = head
                part1 = part1.next
            else:
                part2.next = head
                part2 = part2.next
            head = head.next
        part2.next = None
        part1.next = tmp.next
        return res.next
        