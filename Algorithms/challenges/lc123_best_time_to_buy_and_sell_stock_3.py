"""
Time: O(n)
Space: O(1)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


# DP over 4 states, k=2
# Generalization:
# https://discuss.leetcode.com/topic/107998/most-consistent-ways-of-dealing-with-the-series-of-stock-problems/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cash1 = cash2 = 0  # k=1,2 for the state of cash only
        hold1 = hold2 = -float('inf')  # k=1,2 for the state of holding stock position
        for p in prices:
            cash2 = max(cash2, hold2+p)
            hold2 = max(hold2, cash1-p)
            cash1 = max(cash1, hold1+p)
            hold1 = max(hold1, -p)
        return cash2  # If there is only one peak, hold2 is always equal to hold1
                      # Given you must sell stock 1 before buying stock 2, at the end, the max profit will always be at cash2.
