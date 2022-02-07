class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        res = 0
        i = len(f)-1
        while k>0:
            if k >= f[i]:
                k -= f[i]
                res += 1
            i -= 1
        return res