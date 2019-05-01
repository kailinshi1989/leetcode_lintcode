class TimeMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key2value = {}
        self.key2time = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.key2value:
            self.key2value[key].append(value)
            self.key2time[key].append(timestamp)
        else:
            self.key2value[key] = [value]
            self.key2time[key] = [timestamp]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.key2time:
            return ""
        lo = 0
        hi = len(self.key2time[key]) - 1
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if self.key2time[key][mid] < timestamp:
                lo = mid
            else:
                hi = mid
        p = None # 如果 get 的时间在所有 set 时间之前，应该返回 ”“
        if self.key2time[key][hi] <= timestamp:
            p = hi
        elif self.key2time[key][lo] <= timestamp:
            p = lo
        return self.key2value[key][p] if p is not None else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)