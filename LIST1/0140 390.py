class Solution:
    def lastRemaining(self, n: int) -> int:
        a1 = 1
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0:  # 正向
                a1 += step
            else:  # 反向
                if cnt % 2:
                    a1 += step
            k += 1
            cnt //= 2
            step *= 2
        return a1



