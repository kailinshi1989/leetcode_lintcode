"""
遍历数组，每找到一个局部峰值（只要当前的数字大于后面的一个数字，那么当前数字就看作一个局部峰值，跟前面的数字大小无关），
然后向前遍历所有的值，算出共同的矩形面积，每次对比保留最大值。这里再说下为啥要从局部峰值处理，看题目中的例子，局部峰值为2，6，3，
我们只需在这些局部峰值出进行处理，为啥不用在非局部峰值处统计呢，这是因为非局部峰值处的情况，后面的局部峰值都可以包括，比如1和5，
由于局部峰值6是高于1和5的，所有1和5能组成的矩形，到6这里都能组成，并且还可以加上6本身的一部分组成更大的矩形，
那么就不用费力气去再统计一个1和5处能组成的矩形了
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        result = 0
        stack = []
        heights += [-1]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                highest_index = stack.pop()
                start_index = stack[-1] if stack else -1
                area = heights[highest_index] * (i - start_index - 1)
                result = max(result, area)
            stack.append(i)
        return result