class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for x,y in operations:
            i = dic[x]
            dic.pop(x)
            nums[i] = y
            dic[y] = i
        return nums