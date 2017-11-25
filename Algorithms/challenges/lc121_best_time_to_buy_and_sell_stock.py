"""
Time: O(n)
Space: O(1)


Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


# DP over 2 states, k = 1
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
            hold = max(hold, -p)
        return cash


# Maximum Subarray Problem solved by Kadane's algorithm:
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Is Kadane's algorithm Dyanmic Programming?
# https://stackoverflow.com/questions/16323792/dynamic-programming-aspect-in-kadanes-algorithm
# https://www.quora.com/Is-Kadanes-algorithm-consider-DP-or-not-And-how-to-implement-it-recursively
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = float('inf')
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p - buy)
        return profit


def kadane(returns):
    """
    :param returns: daily returns.
    """
    max_ending_here = max_so_far = returns[0]
    for r in returns[1:]:
        # max subarray "ending here" is either the previous max subarray
        # or the previous max subarray + current return
        max_ending_here = max(r, max_ending_here + r)
        # or
        # max(0, max_ending_here + r)
        # to limit profit non-negative in the case of all negative returns
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
