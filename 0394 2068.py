class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dic1 = {}
        dic2 = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for c in alpha:
            dic1[c] = 0
            dic2[c] = 0

        for c in word1:
            dic1[c] += 1
        for c in word2:
            dic2[c] += 1

        for c in alpha:
            if abs(dic1[c] - dic2[c]) > 3:
                return False
        return True