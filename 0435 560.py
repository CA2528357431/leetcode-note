class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = nums.copy()
        dic = {0: 1}

        res = 0
        s = 0
        for i in range(len(nums)):

            s += nums[i]

            out = s - k
            if out in dic:
                res += dic[out]

            if s not in dic:
                dic[s] = 0
            dic[s] += 1
        return res