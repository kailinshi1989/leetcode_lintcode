class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char2String = {}
        usedString = set()
        return self.dfs(pattern, str, char2String, usedString)

    def dfs(self, pattern, str, char2String, usedString):
        if len(pattern) == 0:
            return len(str) == 0

        char = pattern[0]
        if char in char2String:
            word = char2String[char]
            if str.startswith(word) == False:
                return False
            return self.dfs(pattern[1:], str[len(word):], char2String,
                            usedString)

        for i in range(len(str)):
            word = str[:i + 1]

            if word in usedString:
                continue

            char2String[char] = word
            usedString.add(word)
            if self.dfs(pattern[1:], str[i + 1:], char2String, usedString):
                return True
            del (char2String[char])
            usedString.remove(word)
        return False