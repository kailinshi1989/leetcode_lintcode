class Trie(object):
    def __init__(self):
        self.children = {}
        self.wordList = []

    def insert(self, key, word):
        if len(key) == 0:
            self.wordList.append(word)
            return
        char = key[0]
        if char not in self.children:
            self.children[char] = Trie()
        self.wordList.append(word)
        self.children[char].insert(key[1:], word)

    def prefixWordList(self, prefix):
        if len(prefix) == 0:
            return self.wordList
        char = prefix[0]
        if char not in self.children:
            return []
        return self.children[char].prefixWordList(prefix[1:])


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = Trie()
        for word in words:
            trie.insert(word, word)
        self.result = []
        for word in words:
            self.dfs(words, trie, [word])
        return self.result

    def dfs(self, words, trie, path):
        if len(path) == len(words[0]):
            self.result.append(path[:])
            return
        prefix = ""
        level = len(path)
        for i in range(len(path)):
            prefix += path[i][level]
        prefix_wordList = trie.prefixWordList(prefix)
        if len(prefix_wordList) > 0:
            for word in prefix_wordList:
                self.dfs(words, trie, path + [word])
        else:
            return


"""
方法2：用prefix代替trie
"""


from collections import defaultdict


class Solution2(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        prefix = defaultdict(set)
        self.result = []
        for word in words:
            for i in xrange(len(word)):
                prefix[word[:i + 1]].add(word)
        for word in words:
            self.helper(1, [word], prefix)
        return self.result

    def helper(self, i, tmp, prefix):
        if i == len(tmp[0]):
            self.result.append(tmp)
        else:
            to_find = [row[i] for row in tmp]
            to_find = "".join(to_find)
            for word in prefix[to_find]:
                self.helper(i + 1, tmp + [word], prefix)
