class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res = []
        for x in range(n):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            l = x + 1
            r = n - 1

            while l < r:

                if nums[x] + nums[l] + nums[r] > 0:
                    r -= 1
                    while nums[r] == nums[r + 1] and r - 1 >= 0:
                        r -= 1
                elif nums[x] + nums[l] + nums[r] < 0:
                    l += 1
                    while nums[l] == nums[l - 1] and l + 1 < len(nums):
                        l += 1
                else:
                    res.append([nums[x], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l + 1 < len(nums):
                        l += 1
                    while nums[r] == nums[r + 1] and r - 1 >= 0:
                        r -= 1

        return res

# 为了不重复，先排序，再遍历，使得升序排列
# 固定x后，yz用双指针法
# 找到一个解y也要继续遍历

# 逐注意解决同数问题
# x,y,z如果对应值与x-1,y-1,z-1相同，则comtinue