"""
Time: O(n)
Space: O(1)

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: reverse two lists, and add them like 2. Add Two Numbers
# Time: O(n) Space: O(1)


# Solution 2: push two lists to two stacks and add them
# Time: O(n) Space: O(n)


# Solution 3: Same method as 369. Plus One Linked List
# Carry only affects the closest contiguous 9s
# http://www.cnblogs.com/grandyang/p/6216480.html
# Time: O(n) Space: O(1)
class Solution:
    def get_len(self, head):
        n = 0
        while head:
            n += 1
            head = head.next
        return n

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = self.get_len(l1), self.get_len(l2)
        if n1 < n2:  # set l1 to the longer one
            l1, l2 = l2, l1
            n1, n2 = n2, n1
        ndiff = n1 - n2
        dummy = ListNode(0)

        # Consume the different nodes in the longer list
        cur = dummy
        right = cur  # the right-most non-9 node to current adding node
        while ndiff > 0:
            cur.next = ListNode(l1.val)
            if l1.val != 9:
                right = cur.next
            cur = cur.next
            l1 = l1.next
            ndiff -= 1

        # Add the common parts of two lists
        while l1:
            val = l1.val + l2.val
            if val > 9:  # add carry to left digits until reaching right
                val %= 10
                right.val += 1
                while right.next:  # set all 9 nodes on the left of current adding nodes to 0
                    right.next.val = 0
                    right = right.next
                right = cur
            cur.next = ListNode(val)
            if val != 9:
                right = cur.next
            cur = cur.next
            l1, l2 = l1.next, l2.next

        return dummy if dummy.val == 1 else dummy.next
