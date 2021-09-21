class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        dic = {}
        w = 0
        r = 0
        while r<len(nums):
            if nums[r] not in dic:
                dic[nums[r]] = 1
                nums[w] = nums[r]
                w+=1
            elif dic[nums[r]] == 1:
                dic[nums[r]] += 1
                nums[w] = nums[r]
                w+=1
            r+=1
        return w
        '''

        # 利用有序性
        i = 1
        w = 1
        r = 1
        while r<len(nums):
            if nums[r]==nums[r-1]:
                if i<2:
                    i+=1
                    nums[w] = nums[r]
                    w+=1
            else:
                i=1
                nums[w] = nums[r]
                w+=1

            r+=1

        return w