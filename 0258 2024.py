class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        n = len(a)

        res = 0

        s = 0
        l = 0
        r = 0
        while r < n:
            if a[r] == "T":
                s += 1
            r += 1
            while s > k:
                if a[l] == "T":
                    s -= 1
                l += 1
            res = max(r - l, res)

        s = 0
        l = 0
        r = 0
        while r < n:
            if a[r] == "F":
                s += 1
            r += 1
            while s > k:
                if a[l] == "F":
                    s -= 1
                l += 1
            res = max(r - l, res)

        return res