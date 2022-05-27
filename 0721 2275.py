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

        # https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/solution/c-by-xiao-zhu-xin-meng-nrm7/

        return res