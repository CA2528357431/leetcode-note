class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        li = [ord(x) - ord("a") for x in s]
        n = len(li)
        res = 1

        lim = [0] * 26

        for i in range(n):
            num = li[i]
            l = 1
            for x in range(k + 1):
                if 0 <= num + x < 26:
                    l = max(lim[num + x] + 1, l)
                if 0 <= num - x < 26:
                    l = max(lim[num - x] + 1, l)
            lim[num] = max(lim[num], l)

            res = max(res, l)
            # print(lim)
        return res
