class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        cum = [0] * (n + 1)
        for i in range(n):
            cum[i + 1] = cum[i] + beans[i]

        res = 9999999999999
        for i in range(n):
            if i > 0 and beans[i] == beans[i - 1]:
                continue
            left = cum[i]
            ii = i
            while ii < n and beans[ii] == beans[i]:
                ii += 1
            right = (cum[n] - cum[ii]) - beans[i] * (n - ii)
            res = min(res, left + right)
        return res