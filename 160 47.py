class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i):

            # i之前的已经填写好
            
            if i == len(nums):
                res.append(nums.copy())
            used = set()
            for x in range(i, len(nums)):

                if nums[x] in used:
                    continue
                used.add(nums[x])

                nums[i], nums[x] = nums[x], nums[i]
                dfs(i + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return res