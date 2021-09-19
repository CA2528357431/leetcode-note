class Solution:
    def minSteps(self, n: int) -> int:

        # 动态规划
        '''
        res = [9999]*(n+1)
        res[1] = 0
        for i in range(2,n+1):
            j = 1
            while j*j<=i:
                if i%j==0:
                    res[i] = min(res[i],res[j]+i//j)
                    res[i] = min(res[i],res[i//j]+j)
                # 找因数
                j+=1
        return res[-1]
        '''

        res = 0
        while n>1:
            neo = n//2
            while n%neo:
                neo-=1
            res+=1+(n//neo-1)
            n = neo
        return res

    # 寻找n的最大因数，由此作为下一个n

        i = 2
        res = 0
        while n>1:
            while n%i!=0:
                i+=1
            n = n//i
            res+=i
        return res
    # 寻找所有的质因数求和
    # a-->b的代价为 b//a-1的粘贴 和 1的复制
    # 因此只要依照质因数分解不断变化即可
    # 如n = 90
    # 1 --> 1*2 --> 1*2*3 --> 1*2*3*3 --> 1*2*3*3*5


