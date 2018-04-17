"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


# Quick select
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        while nums:
            pivot = nums[-1]
            q = -1
            for j in range(len(nums)):
                if nums[j] >= pivot:
                    q += 1
                    nums[q], nums[j] = nums[j], nums[q]

            l = q + 1  # s[q] is the l-th order statistic
            if l == k:
                return nums[q]
            elif k < l:
                nums = nums[:q]
            else:
                nums = nums[q+1:]
                k -= l


# heap sort
import heapq
class Solution2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
