class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:

        # BFS

        res = [""]
        for x in s:
            if x.isdigit():
                for i in range(len(res)):
                    res[i] += x
            else:
                ress = res.copy()
                for i in range(len(res)):
                    res[i] += x
                    ress[i] += x.swapcase()
                res.extend(ress)
        return res



