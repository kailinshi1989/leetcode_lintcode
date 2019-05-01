class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        return self.helper(word, self.root)

    def helper(self, word, node):

        if node is None:
            return False

        if len(word) == 0:
            return node.isWord

        if word[0] != '.':
            if word[0] not in node.children:
                return False
            return self.helper(word[1:], node.children[word[0]])

        for child in node.children:
            if self.helper(word[1:], node.children[child]):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)