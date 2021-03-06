"""
Time: O(m+n) using stack and hash table, or O(m*n) with brute force
Space: O(m+n) using stack and hash table, or O(m) with brute force

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number
        for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the
        second array is 3.
    For number 2 in the first array, there is no next greater number for it in
        the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the
        second array is 3.
    For number 4 in the first array, there is no next greater number for it in
        the second array, so output -1.

Note:
1. All elements in nums1 and nums2 are unique.
2. The length of both nums1 and nums2 would not exceed 1000.
"""


class Solution1(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time: O(m*n)
        # Space: O(m)
        nge = []
        for x in findNums:
            loc = nums.index(x)
            found = False
            for y in nums[loc+1:]:
                if y > x:
                    nge.append(y)
                    found = True
                    break
            if not found:
                nge.append(-1)
        return nge


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time: O(m+n)
        # Space: O(m+n). m for hash table, n for stack
        nge_map = {}
        stk = []  # stack

        for y in nums:  # O(2n), push and pop for each y if nums in ascending
            while stk and stk[-1] < y:
                nge_map[stk.pop()] = y
            stk.append(y)

        nge = [nge_map.get(x, -1) for x in findNums]  # O(m)
        return nge
