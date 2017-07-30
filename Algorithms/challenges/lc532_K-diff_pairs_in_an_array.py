"""
Time: O(n)
Space: O(n)
or
Time: O(nlg(n))
Space: O(1)


Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""


from collections import Counter


# hash table. O(n)/O(n)
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = Counter(nums)
        res = 0
        for i in cnt:
            if (k == 0 and cnt[i] > 1) or (k > 0 and (i+k) in cnt):
                res += 1
        return res

    def findPairs2(self, nums, k):
            cnt = Counter(nums)
            return sum(k > 0 and i + k in cnt
                       or k == 0 and cnt[i] > 1
                       for i in cnt)

    def findPairs3(self, nums, k):
        if k > 0:
            return len(set(nums) & {n+k for n in nums})
        else:
            return sum(v > 1 for v in Counter(nums).values())


# sorting and slow/fast pointers. O(nlg(n))/O(1)
# Loop is O(n).
class Solution2(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i = j = 0
        res = 0
        while i < len(nums):
            j = max(j, i + 1)
            while j < n and nums[j] <= nums[i] + k:  # 2nd condition very important
                if nums[j] == nums[i] + k:
                    res += 1
                    break
                j += 1
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
