"""
Time: O(kn)
Space: O(k)


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


# DP over 2*k states, k=arbitary
# Generalization:
# https://discuss.leetcode.com/topic/107998/most-consistent-ways-of-dealing-with-the-series-of-stock-problems/
#
# Optimization:
# The maximum number of profitable transactions is n//2, since a profitable
# transaction takes at least 2 days, given buying price is lower than selling.
# If k >= n//2, the same as case 2: 122.
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n//2:  # same as 122: k=inf
            cash, hold = 0, -float('inf')
            for p in prices:
                cash = max(cash, hold+p)
                hold = max(hold, cash-p)
            return cash
        else:
            cash, hold = [0] * (k+1), [-float('inf')] * (k+1)  # 0 transaction is possible
            for p in prices:
                for i in range(k, 0, -1):  # i=k..1, does not include k = 0
                    cash[i] = max(cash[i], hold[i]+p)
                    hold[i] = max(hold[i], cash[i-1]-p)
            return cash[k]
