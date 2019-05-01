class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                result.append(nums1[n1])
                n1 += 1
                n2 += 1
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
        return result

"""
用hash的方法
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash = {}
        for n in nums1:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        result = []
        for n in nums2:
            if n in hash:
                result.append(n)
                hash[n] -= 1
                if hash[n] == 0:
                    del (hash[n])
        return result