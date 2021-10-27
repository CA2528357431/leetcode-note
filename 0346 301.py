class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        n = len(s)

        res = []

        def dfs(i, cur, count):
            if i == n:

                if count == 0:

                    if not res or len(res[0]) == len(cur):
                        res.append(cur)
                    elif len(res[0]) < len(cur):
                        res.clear()
                        res.append(cur)

                return
            if count == 0:
                dfs(n, cur, count)
            for ind in range(i, n):

                if ind > i and s[ind] == s[ind - 1]:
                    continue

                if s[ind] == "(":
                    dfs(ind + 1, cur + "(", count + 1)
                elif s[ind] == ")":
                    if count > 0:
                        dfs(ind + 1, cur + ")", count - 1)
                else:

                    dfs(ind + 1, cur + s[ind], count)

        dfs(0, "", 0)

        if not res:
            li = [c for c in s if c not in "()"]
            return ["".join(li)]
        return res
    # 同0341的法一