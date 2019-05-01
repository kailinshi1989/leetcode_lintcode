"""
Given a stream of integers and a window size, 
calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
from Queue import Queue
class MovingAverage(object):

    def __init__(self, size):
        self.q = Queue()
        self.size = size
        self.sum = 0

    def next(self, val):
        self.sum += val
        if self.q.qsize() == self.size:
            self.sum -= self.q.get()
        self.q.put(val)
        return self.sum * 1.0 / self.q.qsize()



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

"""
deque 的解法
"""
from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque([])
        self.total = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.total += val
        if len(self.q) > self.size:
            num = self.q.popleft()
            self.total -= num
        return self.total * 1.0 / len(self.q)
