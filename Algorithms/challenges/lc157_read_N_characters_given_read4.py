"""
Time: O(n/4) = O(n)
Space: O(4) = O(1)

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

Note: The read function will only be called once for each test case.
"""


class Solution:
    def read(self, buf, n):
        idx = 0
        buf4 = [""] * 4
        while True:
            k = min(read4(buf4), n-idx)  # curr is the number of chars that reads
            buf[idx:idx+k] = buf4[:k]
            idx += k
            if k != 4 or idx == n:  # return if it reaches the end of file or reaches n
                return idx
