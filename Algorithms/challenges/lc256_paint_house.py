"""
Time: O(n)
Space: O(n)

There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain
color is different. You have to paint all the houses such that no two adjacent
houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3
cost matrix. For example, costs[0][0] is the cost of painting house 0 with
color red; costs[1][2] is the cost of painting house 1 with color green, and so
on... Find the minimum cost to paint all houses.

Note: All costs are positive integers.
"""


# Dynamic programming
# 1. subproblem: minimum cost[:i] and paint[i] != paint[i-1]   -- # of subproblems: n
# 2. guess which color for house i  -- # of guesses: 3
#
# 3. recurrence
#    dp[i][p] = cost[i][p] + min(dp[i-1][(p+1) % 3], dp[i-1][(p+2) % 3])
#    min_cost[i] = min(dp[i][p]) for p in (0,1,2)
#
#    -- base case:
#                  dp[0][p] = cost[0][p]
#                  min_cost[0] = min(dp[0][p] for p in (0,1,2))
#    -- time/subproblem: O(1)
#
# 4  topological order: i = 0, 1, ..., n-1
#    -- total time: O(3 * n) = O(n)
# 5. solve original problem:  dp[n-1] = min(dp[n-1][p] for p in (0,1,2))


def minCost(costs):
    n = len(costs)
    dp = [[0] * 3] * n
    dp[0] = costs[0]  # base case
    for i in range(1, n):
        for p in range(3):
            dp[i][p] = costs[i][p] + min(
                dp[i-1][(p+1) % 3], dp[i-1][(p+2) % 3])
    return min(dp[n-1])


def minCost2(costs):
    prev = [0] * 3
    for cost in costs:
        prev = [cost[i] + min(prev[:i], prev[i+1:]) for i in range(3)]
    return min(prev)
