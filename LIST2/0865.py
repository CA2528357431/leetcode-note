class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] -= i
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 0
            dic[x] += 1
        res = 0
        for k in dic:
            v = dic[k]
            if v > 1:
                neo = v * (v - 1) // 2
                res += neo

        # 看看好数对数量
        # i-nums[i]的值一样则是好数对

        return n * (n - 1) // 2 - res
