class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = 1
        a = 1
        for x in range(n-1):
            c *= (m+n-x-2)
            a *= (x+1)
        return c//a

    # 动态规划法见63
    # 一共m+n-2步，m-1步向下