class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        res = k
        for i in range(n - k + 1):
            cnt = 0
            for ii in range(i, i + k):
                if blocks[ii] == "W":
                    cnt += 1
            res = min(res, cnt)
        return res
