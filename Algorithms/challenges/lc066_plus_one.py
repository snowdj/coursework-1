"""
Time: O(n)
Space: O(1)

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        return digits if digits[0] else [1] + digits


# space O(n)
class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(str(x) for x in digits))
        return [int(i) for i in str(num+1)]


# recursive. space O(n)
def plusOne(self, digits):
    digits = digits or [0]
    last = digits.pop()

    if last == 9:
        return self.plusOne(digits) + [0]
    else:
        return digits + [last + 1]
