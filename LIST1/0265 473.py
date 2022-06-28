class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False

        n = len(matchsticks)

        l = s // 4

        ls = [0, 0, 0, 0]

        matchsticks.sort(reverse=True)

        if matchsticks[0] > l:
            return False

        def dfs(i):
            if i == n:
                return True

            cur = matchsticks[i]
            for ii in range(4):
                if ls[ii] + cur <= l:

                    if ii > 0 and ls[ii] == ls[ii - 1]:
                        continue
                    # 剪枝
                    # 如果加入该桶等效于加入上一个桶，就跳过
                    # 四数之和也有这个用法

                    ls[ii]+=cur
                    x = dfs(i+1)
                    if x:
                        return True
                    ls[ii]-=cur
            return False

        return dfs(0)