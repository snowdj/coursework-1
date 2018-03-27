"""
Time: O(n)
Space: O(1)

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


# DP
# 两个dp数组，其中f[i]表示子数组[0, i]范围内的最大子数组乘积，g[i]表示子数组
# [0, i]范围内的最小子数组乘积，初始化时f[0]和g[0]都初始化为nums[0]，其余都初始
# 化为0。那么从数组的第二个数字开始遍历，那么此时的最大值和最小值只会在这三个数
# 字之间产生，即f[i-1]*nums[i]，g[i-1]*nums[i]，和nums[i]。所以我们用三者中的最
# 大值来更新f[i]，用最小值来更新g[i]，然后用f[i]来更新结果res即可
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = big = small = nums[0]
        for x in nums[1:]:
            big, small = max(x, x*big, x*small), min(x, x*big, x*small)
            maximum = max(maximum, big)
        return maximum


# 1. 当遍历到一个正数时，此时的最大值等于之前的最大值乘以这个正数和当前正数中的较大值，此时的最小值等于之前的最小值乘以这个正数和当前正数中的较小值。
# 2. 当遍历到一个负数时，我们先用一个变量t保存之前的最大值mx，然后此时的最大值等于之前最小值乘以这个负数和当前负数中的较大值，此时的最小值等于之前保存的最大值t乘以这个负数和当前负数中的较小值。
# 3. 在每遍历完一个数时，都要更新最终的最大值。
class Solution2:
    def maxProduct(self, nums):
        maximum = big = small = nums[0]
        for x in nums[1:]:
            if x > 0:
                big, small = max(big * x, x), min(small * x, x)
            else:
                last_big = big
                big, small = max(small * x, x), min(last_big * x, x)
            maximum = max(maximum, big)
        return maximum


# Same as above, but omit the temporary variable
class Solution3:
    def maxProduct(self, nums):
        maximum = big = small = nums[0]
        for x in nums[1:]:
            if x < 0:
                big, small = small, big
            big, small = max(big * x, x), min(small * x, x)
            maximum = max(maximum, big)
        return maximum


# 遍历了两次，一次是正向遍历，一次是反向遍历，相当于正向建立一个累加积数组,
# 每次用出现的最大值更新结果res，然后再反响建立一个累加积数组，再用出现的
# 最大值更新结果res，注意当遇到0的时候，prod要重置为1
class Solution4:
    def maxProduct(self, nums):
        maximum = nums[0]
        # forward
        prod = 1
        for x in nums:
            maximum = max(maximum, prod * x)
            prod = 1 if x == 0 else prod * x

        # backward
        prod = 1
        for x in reversed(nums):
            maximum = max(maximum, prod * x)
            prod = 1 if x == 0 else prod * x
        return maximum
