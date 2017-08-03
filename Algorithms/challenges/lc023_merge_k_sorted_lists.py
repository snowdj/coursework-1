"""
Time: O(n*k*lg(k))
Space: O(k)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n*k^2)  Time limit exceeded. 129/130 cases passed.
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not any(lists):
            return None
        dummy = ListNode(None)
        p = dummy
        while any(lists):  # O(n*k)
            vals = [head.val if head else float('inf') for head in lists]
            minidx = vals.index(min(vals))  # O(k)
            p.next = lists[minidx]
            p, lists[minidx] = p.next, lists[minidx].next
        return dummy.next


# Merge sort. O(n*k*lg(k))
class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not any(lists):
            return None

        def mergeTwoLists(l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            cur = head = ListNode(0)
            while l1 or l2:
                if l1 and (not l2 or l1.val <= l2.val):
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            return head.next

        while len(lists) > 1:  # O(lg(k))
            k = len(lists)
            newlists = []
            for i in range(0, k, 2):  # O(k)
                if i == k-1:  # i is the soly last list.
                    newlists.append(lists[i])
                    break
                newlists.append(mergeTwoLists(lists[i], lists[i+1]))  # O(n1+n2)
            lists = newlists
        return lists[0]


# Use heap or priority queue to find minimum of k values. O(n*k*lg(k))
import heapq


class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        p = dummy
        h = [(l.val, l) for l in lists if l]  # O(k) build heap bottom-up
        heapq.heapify(h)  # O(k)
        while h:  # O(n*k)
            p.next = heapq.heappop(h)[1]  # O(lg(k))
            p = p.next
            if p.next:
                heapq.heappush(h, (p.next.val, p.next))  # O(lg(k))
        return dummy.next
