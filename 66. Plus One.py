class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return []
        n = 1
        i = len(digits) - 1
        while n > 0 and i >= 0:
            num = digits[i]
            n, num = divmod(num + n, 10)
            digits[i] = num
            i -= 1
        if n > 0:
            digits = [n] + digits
        return digits