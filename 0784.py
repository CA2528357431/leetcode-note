class Solution:
    def countAsterisks(self, s: str) -> int:
        j = True
        res = 0
        for c in s:
            if c == "*":
                if j:
                    res += 1
            elif c == "|":
                j = not j
        return res
