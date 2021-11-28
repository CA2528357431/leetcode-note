class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = 0
        same = 0
        for c in nums:
            if c<target:
                less+=1
            elif c==target:
                same+=1
        res = []
        for i in range(same):
            res.append(less+i)
        return res