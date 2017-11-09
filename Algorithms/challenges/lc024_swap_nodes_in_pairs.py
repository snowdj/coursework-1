"""
Time: O(n)
Space: O(1)

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        st = ListNode(None)
        st.next = head
        prv, nxt = st, head.next
        while head and head.next:
            nxt = head.next
            prv.next = head.next
            head.next = head.next.next
            nxt.next = head
            prv = head
            head = head.next
        return st.next
