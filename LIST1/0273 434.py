class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        judge = False
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == " " and s[i + 1] != " " and judge:
                res += 1
            if s[i] != " ":
                judge = True
        if not judge:
            return 0
        return res + 1

