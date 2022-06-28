class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        big = -1
        res = 0
        n = len(nums)

        def dfs(cur, i):

            if i == n:
                nonlocal big
                nonlocal res
                if cur < big:
                    pass
                elif cur > big:
                    big = cur
                    res = 1
                else:
                    res += 1
            else:
                dfs(cur, i + 1)
                dfs(cur | nums[i], i + 1)

        dfs(0, 0)
        return res