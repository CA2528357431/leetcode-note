class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for x in range(len(nums)):
            temp = nums.copy()
            spe = temp[x]
            temp.pop(x)
            re = self.permute(temp)
            for r in re:
                r.append(spe)
            res.extend(re)
        return res