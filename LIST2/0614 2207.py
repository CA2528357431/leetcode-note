class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        cnt = [0] * n
        if text[-1] == pattern[1]:
            cnt[-1] = 1
        for i in range(n - 2, -1, -1):
            c = text[i]
            if c == pattern[1]:
                cnt[i] = cnt[i + 1] + 1
            else:
                cnt[i] = cnt[i + 1]
        res1 = 0
        for i in range(n - 1):
            c = text[i]
            if c == pattern[0]:
                res1 += cnt[i + 1]
        res1 += cnt[0]

        cnt = [0] * n
        if text[0] == pattern[0]:
            cnt[0] = 1
        for i in range(1, n):
            c = text[i]
            if c == pattern[0]:
                cnt[i] = cnt[i - 1] + 1
            else:
                cnt[i] = cnt[i - 1]
        res2 = 0
        for i in range(n - 1, 0, -1):
            c = text[i]
            if c == pattern[1]:
                res2 += cnt[i - 1]
        res2 += cnt[-1]

        return max(res1, res2)