"""
Time: O(m*n)
Space: O(min(m,n)) for DP, or O(1) for combination.

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

https://leetcode.com/static/images/problemset/robot_maze.png

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""


# bottom-up DP. dp[i][j] = dp[i-1][j] + dp[i][j-1]
# use 1-d array to save space.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]


# In total m-1+n-1 steps, choose m-1 downward steps, or n-1 rightward steps.
class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = denom = 1
        k = min(m-1, n-1)
        for i in range(k):
            num *= m-1+n-1-i
            denom *= i+1
        return int(num/denom)

    # use math.factorial (return int) to compute nCk.
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = min(m-1, n-1)
        N = m-1 + n-1
        return math.factorial(N)/math.factorial(k)/math.factorial(N-k)
