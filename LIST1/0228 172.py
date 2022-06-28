class Solution:
    def trailingZeroes(self, n: int) -> int:

        # 找5

        '''
        res = 0
        for x in range(5,n+1,5):
            n = 0
            while x%5==0:
                n+=1
                x=x//5
            res+=n
        return res
        '''

        # 分别检查 5 25 125 ...... 整除的个数  n//25 就是1-n可被25整除的数字的个数
        # 把5算完之后，再算25的时候，每个数虽然有两个5，但其中一个被算5的时候用过
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res