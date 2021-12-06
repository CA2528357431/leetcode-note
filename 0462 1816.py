class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = s.split()
        neo = li[:k]
        return " ".join(neo)