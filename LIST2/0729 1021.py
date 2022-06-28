class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        l = -1
        r = -1
        cnt = 0
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                if cnt == 0:
                    l = i
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    r = i
                    res.append(s[l + 1:r])
        return "".join(res)
