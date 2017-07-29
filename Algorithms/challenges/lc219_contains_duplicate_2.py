"""
Time: O(n)
Space: O(n)

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tbl = {}
        for i, v in enumerate(nums):
            if v in tbl and i - tbl[v] <= k:
                return True
            tbl[v] = i
        return False


class Solution2(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tbl = {}
        for i in range(len(nums)):
            tbl.setdefault(nums[i], []).append(i)
        for _, l in tbl.items():
            if min(map(lambda x, y: x-y, l[1:], l[:-1]) or [k+1]) <= k:
            # if min(map(lambda x, y: x-y, l[1:], l[:-1]), default=k+1) <= k:  # Python3
                return True
        return False
