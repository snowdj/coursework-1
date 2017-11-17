"""
Time: O(n)
Space: O(1)

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""


# iteratively
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        x = 1
        for _ in range(n):
            res.append(x)
            if x * 10 <= n:
                x *= 10
            else:
                if x >= n:
                    x //= 10
                x += 1
                while x % 10 == 0:
                    x //= 10
        return res


# recursively, easier to understand
class Solution2:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(x):
            if x > n:
                return
            res.append(x)
            for i in range(10):
                if x * 10 + i <= n:
                    helper(x * 10 + i)
                else:
                    break

        res = []
        for x in range(1, 10):
            helper(x)
        return res
