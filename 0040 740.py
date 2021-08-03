class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        re = [0]*max(nums)
        for x in nums:
            re[x-1]+=x
        la = 0
        cur = re[0]
        p = 0
        while p<=len(re)-2:
            p+=1
            la,cur = cur,max(cur,la+re[p])
        return cur

    # 获得n的值，就不能获得n±1的值
    # 参考劫匪问题
    # 以n为坐标，值为n的若干个数字的和为财富
    # [2,2,3,4,4,6] 转化为[0*1,2*2,1*3,2*4,0*5,1*6],即[0,4,3,8,0,6]