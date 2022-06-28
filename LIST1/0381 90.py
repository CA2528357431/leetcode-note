class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        res = [[]]
        nums.sort()

        for x in range(len(nums)):
            if x!=0 and nums[x] == nums[x-1]:
                rr = [x.copy() for x in rr]
                for li in rr:
                    li.append(nums[x])
                res.extend(rr)
            else:
                rr = [x.copy() for x in res]
                for li in rr:
                    li.append(nums[x])
                res.extend(rr)
        return res
        '''

        # 按长度来

        res = []
        nums.sort()
        def dfs(path, i):
            res.append(path.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(path, j + 1)
                path.pop()
        dfs([], 0)
        return res