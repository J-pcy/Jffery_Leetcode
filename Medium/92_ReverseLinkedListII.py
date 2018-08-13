"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new = ListNode(0)
        new.next = None
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for i in range(1, m):
            cur = cur.next
        pre = cur
        cur = cur.next
        last = cur
        for i in range(m, n + 1):
            next = cur.next
            cur.next = new.next
            new.next = cur
            cur = next
        pre.next = new.next
        last.next = cur
        return dummy.next
        