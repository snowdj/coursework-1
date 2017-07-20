"""
Time: O(n)
Space: O(1)

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1
        return res


# good for the case when elements to remove are rare
class Solution2(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i], nums[n-1] = nums[n-1], nums[i]  # swap i-th and last element
                n -= 1  # reduce array size by 1 to discard the last element
            else:
                i += 1
        return n
