"""
Time: O(log10(n))
Space: O(1)

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        w, cnt, num = 0, 0, 0
        cnt_last, num_last = cnt, num
        while n > cnt:
            cnt_last, num_last = cnt, num
            cnt = cnt + 9 * 10**w * (w+1)
            num = num + 9 * 10**w
            w += 1
        num = num_last + (n - cnt_last + 1) // w
        dig = (n - cnt_last - 1) % w
        return int(str(num)[dig])


# decrease n on-the-fly.
class Solution2(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        w, cnt, start = 1, 9, 1
        while n > w * cnt:
            n -= w * cnt
            w += 1
            cnt *= 10
            start *= 10
        num = start + (n-1) // w
        dig = (n-1) % w
        return int(str(num)[dig])


# stefan...
class Solution3(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        for digits in range(1, 11):  # 10**9 < 2**31 < 10**10
            first = 10**(digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n/digits)[n % digits])
            n -= 9 * first * digits
