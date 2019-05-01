# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        for itv in intervals:
            if len(heap) == 0:
                heappush(heap, itv.end)
            else:
                if itv.start >= heap[0]:
                    heappop(heap)
                heappush(heap, itv.end)
        return len(heap)
