class Solution:
    def getMaxLen(self, nums):

        # 动态规划

        '''
        pos = [0]*len(nums)
        neg = [0]*len(nums)
        if nums[0]>0:
            pos[0] = 1
        elif nums[0]<0:
            neg[0] = 1
        for x in range(1,len(nums)):
            if nums[x]>0:
                pos[x] = pos[x-1]+1
                if neg[x-1]>0:
                    neg[x] = neg[x-1]+1
                # 当neg长为0时，不可
                # 因为此时只有一个正
            elif nums[x]<0:
                neg[x] = pos[x-1]+1
                if neg[x-1]>0:
                    pos[x] = neg[x-1]+1
                # 当neg长为0时，不可
                # 因为此时只有一个负

        return max(pos)
        '''

        # 内存优化
        # 滚动储存neg

        big = 0
        pos = 0
        neg = 0
        if nums[0] > 0:
            pos = 1
            big = 1
        elif nums[0] < 0:
            neg = 1
        for x in range(1, len(nums)):
            if nums[x] > 0:
                pos += 1
                if neg > 0:
                    neg += 1
                else:
                    neg = 0

            elif nums[x] < 0:
                old = neg
                neg = pos + 1
                if old > 0:
                    pos = old + 1
                else:
                    pos = 0

            else:
                neg = 0
                pos = 0

            big = max(big, pos)
        return big
sol = Solution()
sol.getMaxLen([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2])