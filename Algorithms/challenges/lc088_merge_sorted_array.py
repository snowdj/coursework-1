"""
Time: O(m+n)
Space: O(1)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        cnt = m + n - 1
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[cnt] = nums1[m]
                m -= 1
            else:
                nums1[cnt] = nums2[n]
                n -=1
            cnt -= 1
        while n >= 0:
            nums1[cnt] = nums2[n]
            cnt, n = cnt - 1, n - 1


# combine the two loops above
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m == 0 or nums2[n-1] > nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
