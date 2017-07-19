"""
Time: O(n)
Space: O(1)

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        p1 = sentinel
        while p1.next:
            p2 = p1.next
            while p2.next and p2.val == p2.next.val:
                p2 = p2.next
            if p2 != p1.next:
                p1.next = p2.next
            else:
                p1 = p1.next
        return sentinel.next
