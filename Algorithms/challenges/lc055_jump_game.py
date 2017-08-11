"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


# Bruteforce recursion. O(2^n)/O(n). Time limit exceeded.
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def jump(start):
            if start == n - 1:
                return True
            return any(jump(start+step+1) for step in range(nums[start]))
        return jump(0)


# Simple Dynamic Programming O(n^2) / O(n). Time limit exceeded.


# Optimized DP
class SolutionAC(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        lastgood = n-1
        for i in reversed(range(n)):
            if i + nums[i] >= lastgood:
                lastgood = i
        return lastgood == 0


# Forward by Stefan
# https://discuss.leetcode.com/topic/16704/1-6-lines-o-n-time-o-1-space
def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True


def canJump_oneliner(self, nums):
    return reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1), 1) > 0
