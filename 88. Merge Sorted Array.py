class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        current_index_1 = m - 1
        current_index_2 = n - 1
        current_index = m + n - 1

        while current_index_1 >= 0 and current_index_2 >= 0:
            if nums1[current_index_1] > nums2[current_index_2]:
                nums1[current_index] = nums1[current_index_1]
                current_index -= 1
                current_index_1 -= 1
            else:
                nums1[current_index] = nums2[current_index_2]
                current_index -= 1
                current_index_2 -= 1
        if current_index_2 >= 0:
            nums1[:current_index_2 + 1] = nums2[:current_index_2 + 1]
