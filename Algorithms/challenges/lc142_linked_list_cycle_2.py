"""
Time: O(n)
Space: O(1)
summary: http://www.cnblogs.com/hiddenfox/p/3408931.html

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None

        slow = head  # When two pointers meet for 1st time, move one to head
        while slow != fast:  # When they meet again, that's where the cycle begins.
            slow, fast = slow.next, fast.next
        return fast
