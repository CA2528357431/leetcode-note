class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        dic = set()
        for x in nums:
            dic.add(x)
        i = 1
        while True:
            if i not in dic:
                return i
            else:
                i+=1
        '''

        # 原地算法

        for i in range(len(nums)):

            # 将数字放到应有的位置
            while 1 <= nums[i] <= len(nums):
                index = nums[i] - 1

                if nums[index] == nums[i]:
                    break
                # 防止死锁，如果目标位置数值正常，就不再换了

                nums[index], nums[i] = nums[i], nums[index]

        for x in range(len(nums)):
            if nums[x]!=x+1:
                return x+1
        return len(nums)+1