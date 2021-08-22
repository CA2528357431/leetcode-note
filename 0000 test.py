class Solution:
    def threeSum(self, nums):
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