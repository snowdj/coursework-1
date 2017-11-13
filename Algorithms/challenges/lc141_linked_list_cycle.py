"""
Time: O(n)
Space: O(1)
summary: http://www.cnblogs.com/hiddenfox/p/3408931.html

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# hash table, O(n)/O(n)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tbl = {}
        p = head
        while p:
            if tbl.get(p, 0) > 0:
                return True
            tbl[p] = tbl.get(p, 0) + 1
            p = p.next
        return False


# fast/slow pointers, O(n)/O(1)
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:  # reached tail
        return False
