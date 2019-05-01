class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num
        while num > 9:
            num = list(str(num))
            num = sum(int(n) for n in num)
        return num