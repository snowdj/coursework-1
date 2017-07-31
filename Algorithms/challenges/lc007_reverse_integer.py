"""
Time: O(1)
Space: O(1)

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""


# convert to string
class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0 else 1
        r = int(str(s*x)[::-1])
        return (r < 2**31) * (s*r)


# divide and modulo
# x must be converted to absolute value
# as Python does not have 32-bit signed integer.
class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0 else 1
        x = s * x
        res = 0
        while x != 0:
            res = 10 * res + x % 10
            x //= 10
        return s * res if res < 2**31 else 0
