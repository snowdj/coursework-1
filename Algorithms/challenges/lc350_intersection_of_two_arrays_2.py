"""
# If the given array is not sorted and the memory is unlimited:
#   - Time:  O(m + n)
#   - Space: O(min(m, n))
# elif the given array is already sorted:
#   if m << n or m >> n:
#     - Time:  O(min(m, n) * log(max(m, n)))
#     - Space: O(1)
#   else:
#     - Time:  O(m + n)
#     - Soace: O(1)
# else: (the given array is not sorted and the memory is limited)
#     - Time:  O(max(m, n) * log(max(m, n)))
#     - Space: O(1)

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both
arrays.  The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your
algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is
better?
What if elements of nums2 are stored on disk, and the memory is limited such
that you cannot load all elements into the memory at once?
"""


import collections


class MySolution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        res = []
        for n in c1:
            res += [n] * min(c1[n], c2.get(n, 0))
        return res


# discuss solution
def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())


# follow-up 1: sorted
class MySolutionForSorted(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i+1, j+1
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1
        return res


# If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
# read chunks of array that fit into the memory, and record the intersections.

# If both nums1 and nums2 are so huge that neither fit into the memory, sort
# them individually (external sort), then read 2 elements from each array at a
# time in memory, record intersections.

# follow-up 2: nums2 is big
class MySolutionForBigNums2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        c1 = collections.Counter(nums1)
        for x in nums2:
            if c1.get(x, 0) > 0:
                res.append(x)
                c1[x] -= 1
        return res
