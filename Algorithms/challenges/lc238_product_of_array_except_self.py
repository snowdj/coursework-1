"""
Time: O(n)
Space: O(1)

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        # forward
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        # backward
        right = 1
        for i in reversed(range(n)):
            res[i] *= right
            right *= nums[i]

        return res
