"""
Time: O(n)
Space: O(1)

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
"""


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        grpbeg = 0  # beginning index of a contiguous group
        w = 0  # writing pointer
        for i, c in enumerate(chars):
            if i+1 == n or chars[i+1] != c:  # i is the end of a group
                chars[w] = chars[grpbeg]  # write the 1st letter of the group
                w += 1
                if i > grpbeg:  # group has more than 1 letter
                    grplen = i - grpbeg + 1  # length of this group
                    for digit in str(grplen):  # write the length string
                        chars[w] = digit
                        w += 1
                grpbeg = i + 1  # move grpbeg to the beginning of the next group
        return w
