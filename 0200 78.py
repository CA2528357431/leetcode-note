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

        def do(path, i):
            if i == len(nums):
                res.append(path.copy())
                return
            do(path, i + 1)
            path.append(nums[i])
            do(path, i + 1)
            path.pop()

        do([], 0)
        return res


