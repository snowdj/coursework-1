"""
Time: O(1) if using rolling sum; O(m) if adding all elements every time.
Space: O(1)

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

import collections


class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self._queue = collections.deque(maxlen=size)
        self._sum = 0  # rolling sum

    def next(self, val):
        if len(self._queue) == self._queue.maxlen:
            self._sum -= self._queue.popleft()
        self._queue.append(val)
        self._sum += val
        return self._sum/len(self._queue)
