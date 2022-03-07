class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 0
        if nums[0] - 1 >= k:
            neo = (1 + k) * k // 2
            return neo
        else:
            neo = (1 + nums[0] - 1) * (nums[0] - 1) // 2
            res += neo
            k = k - (nums[0] - 1)

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] - 1 > k:
                neo = (nums[i] + 1 + nums[i] + k) * k // 2
                res += neo
                return res
            elif nums[i] == nums[i + 1]:
                continue

            else:
                neo = (nums[i] + 1 + nums[i + 1] - 1) * (nums[i + 1] - nums[i] - 1) // 2
                res += neo
                k = k - (nums[i + 1] - nums[i] - 1)

        if k > 0:
            neo = (nums[-1] + 1 + nums[-1] + k) * k // 2
            res += neo
        return res