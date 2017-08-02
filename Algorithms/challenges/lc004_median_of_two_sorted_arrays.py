"""
Time: O(lg(m+n))
Space: O(1)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


# Binary search the perfect split point
# https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation/
# https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        if n == 0:
            raise ValueError

        half = (m+n+1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            if i < m and B[j-1] > A[i]:  # i is too small, increase i
                lo = i + 1
            elif i > 0 and A[i-1] > B[j]:  # i is too big, decrease i
                hi = i - 1  # hi = i is also OK.
            else:  # split at i is perfect. Now calculate median.
                # find max value of left side
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])

                if (m+n) % 2 == 1:  # totally odd number of elements
                    return max_of_left  # left side has 1 more than right side

                # find min value of right side
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                # totally even number of elements
                return (max_of_left + min_of_right) / 2.0
