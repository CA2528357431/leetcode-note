class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        res = 0
        for w in words:
            if w[:n]==pref:
                res+=1
        return  res