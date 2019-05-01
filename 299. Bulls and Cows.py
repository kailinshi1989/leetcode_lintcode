from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        hash = {}
        for i in range(len(secret)):
            char = secret[i]
            if char in hash:
                hash[char][0] += 1
                hash[char].append(i)
            else:
                hash[char] = [1, i]

        cowNums = defaultdict(int)
        for i in range(len(guess)):
            char = guess[i]
            if char in hash:
                if hash[char][0] > 0:
                    if i in hash[char][1:]:
                        bull += 1
                    else:
                        cow += 1
                        cowNums[char] += 1
                    hash[char][0] -= 1
                else: # 可能这个 char 已经被cow用了，所以要把 cow 的减去给 bull
                    if cowNums[char] > 0 and i in hash[char][1:]:
                        cow -= 1
                        cowNums[char] -= 1
                        bull += 1
        return str(bull) + 'A' + str(cow) + 'B'
