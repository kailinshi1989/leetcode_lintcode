class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str is None or len(str) == 0:
            return 0
        sign = 1
        result = 0
        i = 0
        if str[i] == '+':
            sign = 1
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1

        for c in str[i:]:
            if c.isdigit():
                result = result * 10 + int(c)
                if result > (1 << 31):
                    break
            else:
                break
        result = result * sign
        if result > (1 << 31) - 1:
            return (1 << 31) - 1
        elif result < -(1 << 31):
            return -(1 << 31)
        else:
            return result


