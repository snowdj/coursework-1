"""
Time: O(m+n)
Space: O(m+k2)  k2 is # of non-unique nums2 elements also in nums1.

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tbl = {x: True for x in nums1}
        return list(set([y for y in nums2 if tbl.get(y, False)]))


class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time is O(m*n) for set intersection in worst case!!!
        """
        return list(set(nums1) & set(nums2))
