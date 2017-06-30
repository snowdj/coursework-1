"""
Time: O(n)
Space: O(1)

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# iteratively
class bestIterSolution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


# recursively  Space:O(n)
class bestRecursiveSolution(object):
    def reverseList(self, head):
        def _reverse(node, prev=None):
            if node is None:
                return prev
            n = node.next
            node.next = prev
            return _reverse(n, node)


# iteratively
class myIterSolution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        newhead = head  # single node case
        prv = cur = head
        while cur.next:
            newhead = ListNode(cur.next.val)
            newhead.next = prv
            cur = cur.next
            prv = newhead
        head.next = None
        return newhead
