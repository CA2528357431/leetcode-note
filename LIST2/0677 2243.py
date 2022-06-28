class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def cnt(string):
            res = 0
            for c in string:
                res += int(c)
            return str(res)

        while len(s) > k:
            i = 0
            nxt = []
            while i < len(s):
                nxt.append(cnt(s[i:i + k]))
                i += k
            s = "".join(nxt)
        return s