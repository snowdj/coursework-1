"""
Time: O(n)
Space: O(1)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""


# DP over 2 states, k=inf
# Generalization:
# https://discuss.leetcode.com/topic/107998/most-consistent-ways-of-dealing-with-the-series-of-stock-problems/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cash, hold = 0, -float('inf')
        cash_pre2 = 0  # cash at day i-2
        for p in prices:
            cash_yesterday = cash
            cash = max(cash, hold+p)
            hold = max(hold, cash_pre2-p)
            cash_pre2 = cash_yesterday
        return cash
