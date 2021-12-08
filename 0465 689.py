class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 求最大和
        # s = [0]*(len(nums)+1)
        # for i in range(len(nums)):
        #     s[i+1] = s[i]+nums[i]
        #
        # li = [[0]*(len(nums)+1) for _ in range(4)]
        # for n in range(1,4):
        #     for ii in range(n*k,len(nums)+1):
        #         li[n][ii] = max(li[n][ii-1],li[n-1][ii-k]+s[ii]-s[ii-k])
        # return li

        s = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s[i + 1] = s[i] + nums[i]
        # 前缀和
        res1 = 0
        res12 = [0, k]
        res123 = [0, k, k * 2]
        # 统计big时对应的状态
        # 为何记录res12而不是res2？
        # big12构成中要求1、2不重叠，而res1+res2的搭配无法保证
        big1 = s[res1 + k] - s[res1]
        big12 = s[res12[0] + k] - s[res12[0]] + s[res12[1] + k] - s[res12[1]]
        big123 = s[res123[0] + k] - s[res123[0]] + s[res123[1] + k] - s[res123[1]] + s[res123[2] + k] - s[res123[2]]
        # 便于计算
        for i in range(len(nums) - 3 * k + 1):
            ii1 = i
            ii2 = i + k
            ii3 = i + k * 2
            s1 = s[ii1 + k] - s[ii1]
            s2 = s[ii2 + k] - s[ii2]
            s3 = s[ii3 + k] - s[ii3]

            if s1 > big1:
                res1 = ii1
                big1 = s[res1 + k] - s[res1]
                # 更新big1 res1
            if s2 + big1 > big12:
                res12 = [res1, ii2]
                big12 = s[res12[0] + k] - s[res12[0]] + s[res12[1] + k] - s[res12[1]]
                # 在新big1的情况下更新big12
                # 此时求的时2个窗口的最大和
                # 如果s2参与构成新的big12，则res12 = [res1,ii2]
            if s3 + big12 > big123:
                res123 = res12 + [ii3]
                big123 = s[res123[0] + k] - s[res123[0]] + s[res123[1] + k] - s[res123[1]] + s[res123[2] + k] - s[
                    res123[2]]
                # 在新big12的情况下更新big123
                # 求big123，思路是 求当前位置的big12+s3，保证不重叠
                # 用dp的思想
        return res123