class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n!=0:
            i+=1
            n = n&(n-1)
            # 删除最后一个1为0
        return i