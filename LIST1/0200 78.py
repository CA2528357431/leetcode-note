class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''
        res = [[]]
        for n in nums:

            rr = [x.copy() for x in res]
            for li in rr:
                li.append(n)
            res.extend(rr)

        return res
        '''

        res = []
        def dfs(path, i):
            res.append(path.copy())
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(path, j + 1)
                path.pop()
        dfs([], 0)
        return res

