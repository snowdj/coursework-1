"""
Time: O(n*k)  k is length of the sequences, at least O(n).
Space: O(k)

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            cnt, now = 0, ''
            for i in range(len(res)):
                cnt += 1
                if i == len(res) - 1 or res[i] != res[i+1]:
                    now += str(cnt) + res[i]
                    cnt = 0
            res = now
        return res


from itertools import groupby


class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in groupby(s))
        return s
