class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 有确定状态的时候用此方法维护各个状态下的值

        '''
        pos = [0]*len(nums)
        neg = [0]*len(nums)
        neg[0] = nums[0]
        pos[0] = nums[0]
        for x in range(1,len(nums)):
            pos[x] = max(pos[x-1]*nums[x],nums[x],neg[x-1]*nums[x])
            neg[x] = min(pos[x-1]*nums[x],nums[x],neg[x-1]*nums[x])
        return max(pos)
        '''

        # 滚动优化

        big = nums[0]
        neg = nums[0]
        pos = nums[0]
        for x in range(1,len(nums)):
            pos,neg = max(pos*nums[x],nums[x],neg*nums[x]),min(pos*nums[x],nums[x],neg*nums[x])
            big = max(big,pos)
        return big

    # 我们需要维护 max 和 min
    # max 来自于 min*cur 和 max*cur 和 cur
