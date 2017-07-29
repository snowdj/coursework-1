"""
Time: O(n)
Space: O(n)

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


from itertools import izip_longest


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry, res = 0, []
        for x, y in izip_longest(reversed(a), reversed(b), fillvalue='0'):
            s = int(x) + int(y) + carry
            res.append(str(s % 2))
            carry = s // 2
        return ('1' if carry else '') + ''.join(reversed(res))


class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2)+int(b, 2))[2:]
