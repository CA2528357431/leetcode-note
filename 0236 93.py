class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []

        res = []
        sol = []

        def do(cur, num):
            if num == 4:
                if cur == n:
                    res.append(".".join(sol))
                return
            if cur == n:
                return
            # 为何是 ==n而不是>=n
            # 最后一次cur+x必然会是n-1

            sol.append(s[cur])
            do(cur + 1, num + 1)
            sol.pop()

            if s[cur] != "0":
                if cur + 1 < n:
                    sol.append(s[cur] + s[cur + 1])
                    do(cur + 2, num + 1)
                    sol.pop()
                if cur + 2 < n:
                    i = s[cur] + s[cur + 1] + s[cur + 2]
                    if int(i) < 256:
                        sol.append(i)
                        do(cur + 3, num + 1)
                        sol.pop()

        do(0, 0)
        return res