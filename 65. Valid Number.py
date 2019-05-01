class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        dot = 0
        digit = 0
        s = s.strip() + " "
        i = 0

        if s[i] in ['+', '-']:
            i += 1

        while s[i].isdigit() or s[i] == '.':  # 前面 s.strip() + " " 是为了防止这里过界
            if i < len(s) and s[i] == '.':
                dot += 1
                if dot > 1:
                    return False
            if i < len(s) and s[i].isdigit():
                digit += 1
            i += 1

        if digit == 0:
            return False

        if s[i] == 'e':
            if s[i + 1] in ['+', '-']:
                i += 1
            sright = s[i + 1:]
            if not sright.strip().isdigit():
                return False
            i += len(sright)
        return len(s) - 1 == i
