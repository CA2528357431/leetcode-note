class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        last = [-1] * n
        first = [-1] * n
        nums = [0] * n

        num = 0
        cur = -1
        for i in range(n):
            c = s[i]
            if c == "|":
                cur = i
                num += 1
            last[i] = cur
            nums[i] = num

        cur = -1
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == "|":
                cur = i
            first[i] = cur

        qn = len(queries)
        res = [0] * qn
        for i in range(len(queries)):
            l, r = queries[i]
            rr = last[r]
            ll = first[l]
            if rr <= ll:
                continue
            else:
                numl, numr = 0, nums[rr]
                if ll > 0:
                    numl = nums[ll - 1]
                res[i] = rr - ll + 1 - (numr - numl)
        return res