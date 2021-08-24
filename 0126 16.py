class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        res = 99999
        nums.sort()
        for x in range(len(nums)):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            l = x + 1
            r = len(nums) - 1

            while l < r:

                if abs(nums[x] + nums[l] + nums[r] - target) < abs(res - target):
                    res = nums[x] + nums[l] + nums[r]
                if nums[x] + nums[l] + nums[r] > target:
                    r -= 1
                    while nums[r] == nums[r + 1] and r-1>=0:
                        r -= 1
                elif nums[x] + nums[l] + nums[r] < target:
                    l += 1
                    while nums[l] == nums[l - 1] and l+1<len(nums):
                        l += 1
                else:
                    return target

        return res

# 优化？
# 跳过重复元素
