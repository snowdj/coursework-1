"""
Time: O(n)
Space: O(1)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


# Dynamic Programming
# 1. subproblems: suffix houses[i:]  -- # subproblems: n
# 2. guess if rob house i or not  -- # guesses: 2
# 3. recurrence: dp[i] = max(houses[i] + dp[i+2], 0 + dp[i+1])
#    -- base case: dp[n] = dp[n+1] = 0
#    -- time/subproblem: O(1)
# 4. topological sort: i = n, n-1, n-2, ..., 0
#    -- total time: O(n)
# 5. solve orignal problem: dp[0]


class Solution(object):
    # space O(n)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n + 2)
        for i in reversed(range(n)):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]

    # space O(1)
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for x in nums:
            last, now = now, max(last + x, now)
        return now
