"""
Time: O(n)
Space: O(1)

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
"""


# O(n)/O(n)
class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = list(nums)
        for i in range(len(nums)):
            nums[(i+k) % len(nums)] = t[i]


# O(n)/O(1)
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or k % n == 0:
            return
        i = start = 0
        cur = nums[i]
        for _ in range(n):
            i = (i+k) % n
            t, nums[i] = nums[i], cur
            if i == start:  # i-th position already rotated
                i, start = i+1, start+1
                cur = nums[i]
            else:
                cur = t


# O(n)/O(1), since reversed is iterator, or using pointers to reverse.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:n-k] = reversed(nums[:n-k])
        nums[n-k:] = reversed(nums[n-k:])
        nums[:] = reversed(nums[:])
