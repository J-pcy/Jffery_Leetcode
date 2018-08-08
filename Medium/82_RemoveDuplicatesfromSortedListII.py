"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new = ListNode(0)
        new.next = head
        pre = new
        while pre.next:
            cur = pre.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if cur != pre.next:
                pre.next = cur.next
            else:
                pre = pre.next
        return new.next
        