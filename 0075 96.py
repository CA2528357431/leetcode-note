class Solution:
    def numTrees(self, n: int) -> int:

        # 产生大量重复计算，超时

        '''
        if n == 1 or n == 0:
            return 1
        ans = 0
        for x in range(1,n+1):
            ans+=self.numTrees(x-1)*self.numTrees(n-x)
        return ans
        '''

        ans = [0]*(n+1)
        ans[0]=ans[1]=1
        for x in range(2,n+1):
            for y in range(1,x+1):
                ans[x]+=ans[y-1]*ans[x-y]
        return ans[-1]