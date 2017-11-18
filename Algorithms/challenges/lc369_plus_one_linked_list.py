"""
Time: O(n)
Space: O(1)


Given a non-negative number represented as a singly linked list of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
"""


# Solution 1: reverse linked list
# O(n) / O(1)
# https://discuss.leetcode.com/topic/49755/short-reverse-increase-reverse
def plusOne(self, head):
    tail = None
    while head:
        head.next, head, tail = tail, head.next, head
    carry = 1
    while tail:
        carry, tail.val = divmod(carry + tail.val, 10)
        if carry and not tail.next:
            tail.next = ListNode(0)
        tail.next, tail, head = head, tail.next, tail
    return head


# Solution 2: two stacks
# O(n) / O(n)


# Solution 3: find the right-most non-9 digit
# O(n) / O(1)
def plusOne3(self, head):
    cur, right = head, None
    while cur:
        if cur.val != 9:
            right = cur
        cur = cur.next

    if right is None:  # all digits are 9
        right = ListNode(0)
        right.next = head
        head = right

    right.val += 1
    cur = right.next
    while cur:
        cur.val = 0
        cur = cur.next

    return head
