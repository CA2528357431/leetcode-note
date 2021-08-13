class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # res[x] 表示以x结尾的max值
        '''
        res = [1]*len(nums)
        for x in range(1,len(nums)):
            for y in range(x):
                if nums[x]>nums[y]:
                    res[x] = max(res[y]+1,res[x])
        return max(res)
        '''


        # res[x]代表 "已遍历的序列中" "长度为x+1" 的子序列的末尾的 "最小值”
        # 逻辑可知，越长的子列，末尾数字越大
        # 遍历到新元素时，
        # 如果其大于res[-1]，则最长子序列增长
        # 如果不，则遍历res元素，调整 "最小末尾值”

        res = [nums[0]]
        for x in range(1,len(nums)):
            if nums[x]>res[-1]:
                res.append(nums[x])
            else:
                if nums[x]<res[0]:
                    res[0] = nums[x]
                    # 按照for循环，会无法调整res[0]
                else:
                    for y in range(len(res)-1):
                        if res[y]<nums[x] and nums[x]<res[y+1]:
                            res[y+1]=nums[x]
                            break

        return len(res)


