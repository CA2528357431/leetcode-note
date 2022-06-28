class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = [0]*(target+1)
        res[0] = 1
        for x in range(1,len(res)):
            for y in nums:
                if x-y>=0:
                    res[x]+=res[x-y]
        return res[-1]