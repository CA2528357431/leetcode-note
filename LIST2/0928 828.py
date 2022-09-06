class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        post = [n] * n
        pre = [-1] * n
        dic = {}
        for i in range(n):
            c = s[i]
            if c in dic:
                pre[i] = dic[c]
            dic[c] = i
        dic = {}
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c in dic:
                post[i] = dic[c]
            dic[c] = i

        res = 0
        for i in range(n):
            prex = i - pre[i] - 1
            postx = post[i] - i - 1
            neo = (prex + 1) * (postx + 1)
            res += neo
        return res
