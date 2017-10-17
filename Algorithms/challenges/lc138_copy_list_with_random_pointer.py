"""
Time: O(n)
Space: O(n)

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


from collections import defaultdict


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# O(2n)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        m = {}
        p = head
        while p:
            m[p] = RandomListNode(p.label)
            p = p.next
        p = head
        while p:
            m[p].next = m.get(p.next)
            m[p].random = m.get(p.random)
            p = p.next
        return m.get(head)


# O(n) using defaultdict
class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        m = defaultdict(RandomListNode(0))  # use lambda: class() for Python2
        m[None] = None

        p = head
        while p:
            m[p].label = p.label
            m[p].next = m[p.next]
            m[p].random = m[p.random]
            p = p.next
        return m[head]
