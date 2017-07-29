"""
Time: O()
Space:

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, nA = headA, 0
        while p:
            p, nA = p.next, nA + 1
        p, nB = headB, 0
        while p:
            p, nB = p.next, nB + 1
        ps = [headA, headB][nA > nB]
        pl = [headB, headA][nA > nB]
        for _ in range(max(nA, nB)-min(nA, nB)):
            pl = pl.next
        while ps is not pl:
            ps, pl = ps.next, pl.next
        return ps if ps else None


# two pointers, each travels over unique pathA + unique pathB + path_common.
class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
