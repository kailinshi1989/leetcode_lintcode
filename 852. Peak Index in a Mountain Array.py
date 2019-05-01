class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(A) - 1
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if A[mid] < A[mid + 1]:
                lo = mid
            else:
                hi = mid
        if A[lo] > A[hi]:
            return lo
        else:
            return hi