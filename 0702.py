class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dic = {}

        def do(n, t):
            if (n, t) in dic:
                return dic[(n, t)]
            if t == 0:
                dic[(n, t)] = 1
                return 1

            neo = 0
            if t <= n:
                for i in range(1, t + 1):
                    neo += do(n, t - i)
            else:
                for i in range(1, n + 1):
                    neo += do(n, t - i)
            neo = neo % 1000000007
            dic[(n, t)] = neo
            return neo

        numchar = {"2": 3, "3": 3, "4": 3, "5": 3, "6": 3, "7": 4, "8": 3, "9": 4}

        cur = pressedKeys[0]
        cnt = 0

        li = []
        for c in pressedKeys:
            if cur != c:
                li.append((cur, cnt))
                cur = c
                cnt = 1
            else:
                cnt += 1
        li.append((cur, cnt))

        res = 1

        for c, t in li:
            n = numchar[c]
            neo = do(n, t)
            res *= neo
            res %= 1000000007

        return res % 1000000007