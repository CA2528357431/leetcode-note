class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        # 对于每一位置节点都全面搜索其后的所有位置
        '''
        res=[]
        sol=[]
        n=len(nums)
        def dfs(cur):
            if cur==n:
                if len(sol)>1:
                    res.append(sol.copy())
                return
            dfs(n)
            used=set()
            for i in range(cur,n):
                if (not sol or sol[-1]<=nums[i] )and nums[i] not in used:
                    used.add(nums[i])
                    sol.append(nums[i])
                    dfs(i+1)
                    sol.pop()
        dfs(0)
        return res
        '''

        # 对于每一位置节点，之搜索当前位置
        res = []
        sol = []
        n = len(nums)

        def dfs(cur, used):
            if cur == n:
                if len(sol) > 1:
                    res.append(sol.copy())
                return

            if (not sol or sol[-1] <= nums[cur]) and nums[cur] not in used:
                used.add(nums[cur])
                sol.append(nums[cur])
                dfs(cur + 1, set())
                sol.pop()

                used.add(nums[cur])
                # 去重

            dfs(cur + 1, used)

        dfs(0, set())
        return res
