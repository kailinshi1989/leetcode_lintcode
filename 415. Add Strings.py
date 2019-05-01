class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        num = 0
        while num1 or num2 or num:
            if num1:
                num += int(num1[-1])
                num1 = num1[:-1]
            if num2:
                num += int(num2[-1])
                num2 = num2[:-1]
            num, rem = divmod(num, 10)
            result = str(rem) + result
        return result
