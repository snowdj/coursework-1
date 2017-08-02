"""
Time: O(n^2)
Space: O(1)

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# Scan array, and solve each by sorted 2-sum.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()

        for k in range(n):
            if nums[k] > 0:  # scanning negatives only is enough, because target is mirror.
                break
            if k > 0 and nums[k] == nums[k-1]:  # skip repetitions
                continue
            target = -nums[k]
            i, j = k+1, n-1

            # two pointers scanning for sorted 2-sum problem
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i+1] == nums[i]:
                        i += 1
                    while i < j and nums[j-1] == nums[j]:
                        j -= 1
                    i, j = i+1, j-1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res
