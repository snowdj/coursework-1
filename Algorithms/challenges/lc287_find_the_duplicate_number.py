"""
Time: O(n)
Space: O(1)
http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
http://www.cnblogs.com/hiddenfox/p/3408931.html
https://en.wikipedia.org/wiki/Cycle_detection#Floyd.27s_Tortoise_and_Hare

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


# Floyd's cycle-finding algorithm, or tortoise and hare algorithm
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the 1st-meet point
        tort = nums[0]
        hare = nums[nums[0]]
        while tort != hare:
            tort = nums[tort]
            hare = nums[nums[hare]]

        # place tortoise back to the beginning, and find the cycle beginning
        tort = 0
        while tort != hare:
            tort = nums[tort]
            hare = nums[hare]

        return tort


# Binary search
class Solution3:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low
