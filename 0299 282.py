class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        sol = []
        n = len(num)

        def dfs(i, cal, la):
            if i == n:
                if cal == target:
                    res.append("".join(sol))
                return
            cur = ""
            for j in range(i, n):

                if j > i and num[i] == '0':
                    break

                cur = cur + num[j]
                curint = int(cur)

                if i == 0:
                    sol.append(cur)
                    dfs(j + 1, curint, curint)
                    sol.pop()
                else:

                    # +
                    sol.append("+")
                    sol.append(cur)
                    dfs(j + 1, cal + curint, curint)
                    sol.pop()
                    sol.pop()

                    # -
                    sol.append("-")
                    sol.append(cur)
                    dfs(j + 1, cal - curint, -curint)
                    sol.pop()
                    sol.pop()

                    # *
                    sol.append("*")
                    sol.append(cur)
                    dfs(j + 1, cal - la + la * curint, la * curint)
                    sol.pop()
                    sol.pop()

        dfs(0, 0, 0)
        return res