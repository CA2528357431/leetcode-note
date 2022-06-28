class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cur = {0: 1}

        for n in nums:
            neo = {}
            for pre in cur:
                neo[pre + n] = neo.get(pre + n, 0) + cur[pre]
                neo[pre - n] = neo.get(pre - n, 0) + cur[pre]
            cur = neo

        if target in cur:
            return cur[target]
        return 0