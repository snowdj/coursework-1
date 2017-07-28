"""
Time: O(n)
Space: O(n) or O(1)

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Use slow/fast pointers to find middle,
# then use a stack to reverse first half list.
# O(1)/O(n)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        stk = [head]
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            stk.append(slow)
        if not fast.next:  # In the case of odd number of nodes, remove the middle one.
            stk.pop()
        while slow.next:
            slow = slow.next
            if slow.val != stk.pop().val:
                return False
        return True


# Use slow/fast pointers to find middle,
# then reverse the 2nd half list in place.
# O(1)/O(1)
class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # reverse the 2nd half list
        last, now = slow.next, slow.next.next
        while last.next:
            last.next, now.next = now.next, slow.next
            slow.next, now = now, last.next
        # compare the 1st and the reversed 2nd half lists
        while slow.next:
            slow = slow.next
            if head.val != slow.val:
                return False
            head = head.next
        return True


# brute-force. Reverse the whole list in place, and save to a new list.
