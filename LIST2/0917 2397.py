class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:

        def cnt(n):
            res = 0
            while n:
                n &= n - 1
                res += 1
            return res

        def get(li):
            cur = 0
            for x in li:
                cur = cur * 2 + x
            return cur

        m = len(mat)
        n = len(mat[0])

        li = [get(x) for x in mat]

        res = 0

        for i in range(2 ** n):
            if cnt(i) > cols:
                continue
            cur = 0
            for x in li:
                if (i & x) == x:
                    cur += 1

            res = max(res, cur)
        return res
