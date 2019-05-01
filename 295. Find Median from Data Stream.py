"""
把比 median 小的放在 maxheap 里，把比 median 大的放在 minheap 里。median 单独放在一个变量里。
每次新增一个数的时候，先根据比当前的 median 大还是小丢到对应的 heap 里。
丢完以后，再处理左右两边的平衡性:

如果左边太少了，就把 median 丢到左边，从右边拿一个最小的出来作为 median。
如果右边太少了，就把 median 丢到右边，从左边拿一个最大的出来作为新的 median。

maxHeap里面的是负数，minHeap里面的是正数
"""
from heapq import *


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.med = None
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.med is None or num < self.med:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        self.balance()

    def findMedian(self):
        """
        :rtype: float
        """
        return self.med

    def balance(self):
        while len(self.minHeap) - len(self.maxHeap) > 1:
            num = heappop(self.minHeap)
            heappush(self.maxHeap, -num)

        while len(self.maxHeap) - len(self.minHeap) > 1:
            num = heappop(self.maxHeap)
            heappush(self.minHeap, -num)
            
        if len(self.minHeap) == len(self.maxHeap):
            self.med = (self.minHeap[0] - self.maxHeap[0]) / 2.0
        elif len(self.minHeap) > len(self.maxHeap):
            self.med = self.minHeap[0]
        else:
            self.med = -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()