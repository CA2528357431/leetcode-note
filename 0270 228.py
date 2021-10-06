class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        cur = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > cur[1] + 1:
                if cur[0] == cur[1]:
                    res.append(str(cur[0]))
                else:
                    res.append(str(cur[0]) + "->" + str(cur[1]))
                cur[0], cur[1] = nums[i], nums[i]
            else:
                cur[1] = nums[i]
        if cur[0] == cur[1]:
            res.append(str(cur[0]))
        else:
            res.append(str(cur[0]) + "->" + str(cur[1]))
        return res
