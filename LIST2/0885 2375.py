class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)

        def find(x):
            dec = 0
            for i in range(x, n):
                if pattern[i] == "I":
                    return dec
                else:
                    dec += 1

            return dec

        li = [find(x) for x in range(n + 1)]
        res = []
        use = list(range(1, 10))
        for small in li:
            res.append(str(use[small]))
            use.pop(small)
        return "".join(res)

    # 只有确定更小的数字算作更小