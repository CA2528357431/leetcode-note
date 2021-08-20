class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # 2**30 最大的2**n
        '''
        return n>0 and 2**30%n==0
        '''

        # 位运算 A
        '''
        return n>0 and n&(n-1)==0
        '''

        # 位运算 B
        return n>0 and n&(-n)==n

