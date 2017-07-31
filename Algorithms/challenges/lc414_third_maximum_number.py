"""
Time: O(n)
Space: O(1)

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


import bisect


# using set, as set(list()) is O(n) assuming no hashing collision.
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        s = sorted(nums[:3])
        for x in nums[3:]:
            bisect.insort(s, x)
            s = s[1:]  # gurantee O(lg(3)) instead of O(lg(n))
        return s[0] if len(s) == 3 else s[-1]


class Solution2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            s.remove(max(s))
            s.remove(max(s))
            return max(s)


# manually insertion
class Solution3(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]
