class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            res.append(s[i:i+k])
            i+=k
        if len(res[-1])<k:
            res[-1] = res[-1]+fill*(k-len(res[-1]))
        return res