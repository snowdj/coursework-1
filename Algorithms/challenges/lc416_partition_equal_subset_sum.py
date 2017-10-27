"""
Time: O(N*sum(nums))
Space: O(sum(nums))

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


# Partition problem: https://en.wikipedia.org/wiki/Partition_problem
# 0/1 knapsack: https://discuss.leetcode.com/topic/67539/0-1-knapsack-detailed-explanation
# General subset sum problem: https://en.wikipedia.org/wiki/Subset_sum_problem
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) & 1:
            return False
        half = sum(nums) // 2
        dp = [False] * (half+1)
        dp[0] = True
        for x in nums:
            for target in range(half, x-1, -1):
                    dp[target] = dp[target] or dp[target-x]
        return dp[half]


# Recursive DP, or DFS + memoization
class Solution2(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) & 1:
            return False
        n = len(nums)
        half = sum(nums) // 2
        m = [[None] * (n+1) for _ in range(half+1)]

        def dp(target, i):
            if target == 0:
                return True
            elif target < 0 or i < 0:
                return False
            else:
                if m[target][i] is None:
                    m[target][i] = dp(target, i-1) or dp(target-nums[i-1], i-1)
                return m[target][i]
        return dp(half, len(nums))


# Same as solution1, but use bits to represent DP column.
# Very fast.
class Solution3(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) & 1:
            return False
        half = sum(nums) // 2
        dp = 1
        for x in nums:
            dp = dp << x | dp
        return bool(dp >> half & 1)
