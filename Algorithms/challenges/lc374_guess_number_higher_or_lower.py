"""
Time: O(lg(n))
Space: O(1) iterative, O(lg(n)) recursive

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass


# recursively
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binsearch(low, high):
            if low == high:
                return low
            mid = (low + high) // 2
            return binsearch(mid+1, high) if guess(mid) > 0 else binsearch(low, mid)
        return binsearch(1, n)


# iteratively
class Solution2(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            low, high = [(low, mid), (mid+1, high), (low, mid)][guess(mid)]
        return low
