class Solution:
    def countSpecialNumbers(self, n: int) -> int:

        s = str(n)

        dp = [0] * 10
        dp[0] = 9
        ava = 9
        for i in range(1, 10):
            dp[i] = dp[i - 1] * ava
            ava -= 1

        length = len(s)
        res = sum(dp[:length - 1])

        dic = {}

        # 在放置x位数字时，已用数字有li，是否被限制状态时lim
        # li用二进制表示数字状态
        # 如处理4321时，已经填写了4、43、432时，就是被限制
        def do(x, li, lim):
            if x == len(s):
                return 1
            if (x, li, lim) in dic:
                return dic[(x, li, lim)]

            if lim:
                res = 0
                num = int(s[x])
                for i in range(num):
                    if (1 << i) & li != 0:
                        continue
                    res += do(x + 1, li | (1 << i), False)
                if (1 << num) & li == 0:
                    res += do(x + 1, li | (1 << num), True)
                dic[(x, li, lim)] = res
                return res

            if not lim:
                res = 0
                for i in range(10):
                    if (1 << i) & li != 0:
                        continue
                    res += do(x + 1, li | (1 << i), False)
                dic[(x, li, lim)] = res
                return res

        num = int(s[0])
        for i in range(1, num):
            neo = do(1, 1 << i, False)
            res += neo
        res += do(1, 1 << num, True)

        return res
