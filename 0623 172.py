class Solution:
    def trailingZeroes(self, n: int) -> int:
        find2 = 2
        cnt2 = 0
        while find2 <= n:
            cnt2 += n // find2
            find2 *= 2
        find5 = 5
        cnt5 = 0
        while find5 <= n:
            cnt5 += n // find5
            find5 *= 5

        return min(cnt2, cnt5)