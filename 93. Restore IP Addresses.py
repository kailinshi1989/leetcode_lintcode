"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

所以说IP地址总共有四段，每一段可能有一位，两位或者三位，范围是[0, 255]，
题目明确指出输入字符串只含有数字，所以当某段是三位时，
我们要判断其是否越界（>255)，还有一点很重要的是，当只有一位时，0可以成某一段，
如果有两位或三位时，像 00， 01， 001， 011， 000等都是不合法的，
所以我们还是需要有一个判定函数来判断某个字符串是否合法。
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, path):
        if len(path) == 4:
            if len(s) == 0:
                self.result.append('.'.join(path[:]))
            return
        if len(s) == 0:
            return
        for i in range(1, min(4, len(s) + 1)):
            sub_string = s[:i]
            if int(sub_string) <= 255 and (sub_string[0] != '0' or len(sub_string) == 1): # "0000" => ["0.0.0.0"] 要考虑这种特殊情况
                self.dfs(s[i:], path + [sub_string])