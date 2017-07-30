"""
Time: O(1)
Space: O(1)

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        for _ in range(32):
            r = (r << 1) + (n & 1)
            n >>= 1
        return r


# optimize: divide 32-bit integer to 4 bytes, and
# cache the reversed bytes.
# https://discuss.leetcode.com/topic/9764/java-solution-and-optimization


# Divide-and-Conquer.
# If multi-bit shift per instruction is allowed, this method uses less clock
# cycles, 10 vs 32.
class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
