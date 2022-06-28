class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        if n == 0:
            return 0

        def check(r):
            num = 0
            while r > 0:
                if r % 10 == 1:
                    num += 1
                r = r // 10
            return num

        cur = 0
        for x in range(n):
            cur += check(x + 1)

        return cur
        '''

        # 按位计算

        num = 0
        p = 1
        while p<=n:

            big = n//(p*10)*(p)

            if n//p%10==0:
                small = 0
            elif n//p%10==1:
                small = n%p+1
            else:
                small = p

            num+=big
            num+=small

            p = p*10
        return num
    # https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode-solution-zopq/