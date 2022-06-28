class Solution:
    def greatestLetter(self, s: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for c in alpha[::-1]:
            if c in s and c.upper() in s:
                return c.upper()
        return ""