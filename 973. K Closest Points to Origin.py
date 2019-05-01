import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            d = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-d, point))
            while len(heap) > K:
                heapq.heappop(heap)
        result = []
        while len(heap) > 0:
            point = heapq.heappop(heap)
            result.append(point[1])
        return result
