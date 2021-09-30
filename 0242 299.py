class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i = 0

        A = 0
        B = 0

        dic = {}
        for c in secret:
            dic[c] = dic.get(c, 0) + 1

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
                dic[guess[i]] -= 1
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in dic and dic[guess[i]] > 0:
                B += 1
                dic[guess[i]] -= 1

        return str(A) + "A" + str(B) + "B"