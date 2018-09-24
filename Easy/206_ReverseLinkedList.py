"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        if not head or not head.next:
            return head
        tmp = head.next
        node = self.reverseList(tmp)
        head.next = None
        tmp.next = head
        return node
        """
        """
        if not head or not head.next:
            return head
        tmp = [None]
        cur = head
        while cur:
            tmp.append(cur)
            cur = cur.next
        dummy = ListNode(0)
        cur = dummy
        for node in reversed(tmp):
            cur.next = node
            cur = cur.next
        return dummy.next
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
        