class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
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
        '''

        res = []

        def dfs(i):

            # i之前的已经填写好

            if i == len(nums):
                res.append(nums.copy())
                return
            for x in range(i, len(nums)):
                nums[x], nums[i] = nums[i], nums[x]

                dfs(i + 1)

                nums[x], nums[i] = nums[i], nums[x]

        dfs(0)
        return res

# 为了防止改变res，引入copy()