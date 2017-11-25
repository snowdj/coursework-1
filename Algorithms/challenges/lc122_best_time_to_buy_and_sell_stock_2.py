"""
Time: O(n)
Space: O(1)

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
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
        for p in prices:
            cash = max(cash, hold+p)
            hold = max(hold, cash-p)
        return cash


# Another way
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i+1] - prices[i], 0)
                   for i in range(len(prices) - 1))
