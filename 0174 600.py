class Solution:
    def findIntegers(self, n: int) -> int:

        '''
        res = 0

        length = len(bin(n))-2

        def dfs(pre,height,num):

            nonlocal res

            if pre == 1:
                if height==0:
                    res+=1
                    return
                else:
                    dfs(0,height-1,num)
            else:
                if height==0:
                    res+=1
                    if num+1<=n:
                        res+=1
                    return
                else:
                    dfs(0,height-1,num)
                    if num+2**height<=n:
                        dfs(1,height-1,num+2**height)
        dfs(0,length-1,0)
        return res
        '''

        # https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/solution/shu-wei-dpmo-ban-ji-jie-fa-by-initness-let3/
        if n == 1:
            return 2
        if n == 0:
            return 1

        l = len(bin(n)) - 2

        res = 0

        pre = 0

        dp = [0] * (l)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, l):
            dp[i] = dp[i - 1] + dp[i - 2]
            # 长度为i的且符合长度的的二进制数字

        for i in range(l)[::-1]:
    #   for i in range(l-1,-1,-1):   这样似乎更快

            val = (n >> i) & 1
            if val:
                res += dp[i]

                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0
        else:
            res += 1
            # 如果没有break，则最后一位填上原数字后没有计入

        return res