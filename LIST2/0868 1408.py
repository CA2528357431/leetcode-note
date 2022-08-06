class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            for j in words:
                if i==j:
                    continue
                if i in j:
                    res.append(i)
                    break
        return res