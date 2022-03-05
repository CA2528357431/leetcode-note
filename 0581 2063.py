class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        n = len(word)
        for i in range(n):
            if word[i] in "aeiou":
                l = i-0+1
                r = n-1-i+1
                res+=l*r
        return res