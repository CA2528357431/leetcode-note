class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        big = 2 ** 31
        if n <= 0:
            return False
        if big % n:
            return False

        # 确认是二进制下只有一个数字

        mark = 0
        s = 1
        for i in range(16):
            mark += s
            s *= 4
        if mark & n == 0:
            return False
        else:
            return True