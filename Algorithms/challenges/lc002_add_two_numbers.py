"""
Time: O(n)
Space: O(1) iteratively, O(n) recursively.

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Follow up:
What if the the digits in the linked list are stored in non-reversed order? For example:
(3→4→2)+(4→6→5)=8→0→7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Tail recursion
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def helper(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            l1_val, l1_next = (l1.val, l1.next) if l1 else (0, None)
            l2_val, l2_next = (l2.val, l2.next) if l2 else (0, None)
            s = ListNode((l1_val+l2_val+carry) % 10)
            carry = (l1_val+l2_val+carry) // 10
            s.next = helper(l1_next, l2_next, carry)
            return s
        return helper(l1, l2, 0)


# Iteratively
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = s = ListNode(None)
        while l1 or l2 or carry:
            t = 0
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            s.next = ListNode((t+carry) % 10)
            carry = (t+carry) // 10
            s = s.next
        return head.next


# follow up: use two stacks to store l1, l2 and solve it iteratively.
