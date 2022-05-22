class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0

        for i in range(30):
            cur = 0
            st = 1 << i
            for x in candidates:
                if x & st > 0:
                    cur += 1
            res = max(res, cur)

        return res