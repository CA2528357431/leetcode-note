class Solution:
    def repeatedCharacter(self, s: str) -> str:
        se = set()
        for c in s:
            if c in se:
                return c
            else:
                se.add(c)