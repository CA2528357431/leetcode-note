class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for x in range(n):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            z = n - 1
            for y in range(x + 1, n):
                if y != x + 1 and nums[y] == nums[y - 1]:
                    continue
                while nums[x] + nums[y] + nums[z] > 0 and y < z:
                    z -= 1
                if y >= z:
                    break

                elif nums[x] + nums[y] + nums[z] == 0:
                    res.append([nums[x], nums[y], nums[z]])

        return res

# 为了不重复，先排序，再遍历，使得升序排列
# 固定x后，yz用双指针法
# 随着y变大，z只能变小
# 然而传统双指针只能判定有无，因此及时找到一个解y也要继续遍历

# 逐注意解决同数问题
# x,y如果对应值与x-1,y-1相同，则comtinue
# 由于每对xy只有一个值成立，成立或条件不符合直接break，因此z不会重复