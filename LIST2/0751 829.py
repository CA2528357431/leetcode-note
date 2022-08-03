class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, l: int) -> bool:
            if l % 2==1:
                return n%l == 0
            else:
                return n%l == l//2

        res = 0
        l = 1
        while l * (l + 1) <= n * 2:
            if isKConsecutive(n, l):
                res += 1
            l += 1
        return res