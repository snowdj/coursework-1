"""
Time: O(n)
Space: O(1)
https://en.wikipedia.org/wiki/Dutch_national_flag_problem

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""


# Head/Tail 2 pointers with swapping.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        head, tail = 0, n-1
        i = 0
        while i <= tail:
            if nums[i] == 0:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1
                i += 1
            elif nums[i] == 2:
                nums[tail], nums[i] = nums[i], nums[tail]
                tail -= 1
            else:
                i += 1


# Emulate quicksort.
# Keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k).
# We don't need to swap because we know the values we want.
# https://discuss.leetcode.com/topic/26181/ac-python-in-place-one-pass-solution-o-n-time-o-1-space-no-swap-no-count/2
def sortColors(self, nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
