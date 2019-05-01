# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

import random


class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        i = 0
        match = 0
        while i < 10 and match < 6 and len(wordlist) > 0:
            pick_word = wordlist[random.randint(0, len(wordlist) - 1)]
            match = master.guess(pick_word)
            stack = []
            for word in wordlist:
                if self.matchCompare(word, pick_word) == match:
                    stack.append(word)
            wordlist = stack

    def matchCompare(self, word_1, word_2):
        result = 0
        for i in range(len(word_1)):
            if word_1[i] == word_2[i]:
                result += 1
        return result
