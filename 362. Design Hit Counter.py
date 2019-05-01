class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        total = 0
        for i in xrange(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total


"""
方法 2
"""


import bisect


class HitCounter2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        lo = max(0, timestamp - 300)
        start_index = bisect.bisect_right(self.hits, lo)
        end_index = bisect.bisect_right(self.hits, timestamp)
        return end_index - start_index


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
