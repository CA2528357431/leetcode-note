class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        dic = {}

        for p, b in items:
            if p not in dic:
                dic[p] = -1
            dic[p] = max(dic[p], b)
        n = len(queries)
        res = [0] * n

        ps = list(dic.keys())
        ps.sort()

        for i in range(1, len(ps)):
            p = ps[i]
            lp = ps[i - 1]
            dic[p] = max(dic[p], dic[lp])

        for i in range(n):
            q = queries[i]
            if q in dic:
                res[i] = dic[q]
                continue

            if q > ps[-1]:
                res[i] = dic[ps[-1]]
            elif q < ps[0]:
                res[i] = 0
            else:

                l = 0
                r = len(ps) - 1
                while l < r:
                    mid = (l + r) // 2 + 1
                    if q < ps[mid]:
                        r = mid - 1
                    elif ps[mid] < q:
                        l = mid
                res[i] = dic[ps[l]]

        return res