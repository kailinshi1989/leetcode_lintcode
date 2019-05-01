"""
方法1：greedy，只要是有增加的都要
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        result = 0
        for i in range(1, len(prices)):
            result += max(0, prices[i] - prices[i - 1])
        return result



"""
方法2：两个指针保存lo，hi
"""



class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        result = 0
        lo, hi = sys.maxint, sys.maxint
        for p in prices:
            if p > hi:
                hi = p
            else:
                result += hi - lo
                hi, lo = p, p
        return result + hi - lo