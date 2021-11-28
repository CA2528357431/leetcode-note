class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)

        if n < m:
            return []

        alpha = "abcdefghijklmnopqrstuvwxyz"

        stand = {c: 0 for c in alpha}
        for c in p:
            stand[c] += 1

        cur = {c: 0 for c in alpha}
        for i in range(m - 1):
            cur[s[i]] += 1

        res = []
        for i in range(m - 1, n):
            cur[s[i]] += 1
            if cur == stand:
                res.append(i - m + 1)
            cur[s[i - m + 1]] -= 1
        return res