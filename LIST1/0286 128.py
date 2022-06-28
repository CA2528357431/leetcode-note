class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        res = 0
        for num in dic:
            if num - 1 not in dic:
                cur = num

                while cur in dic:
                    cur += 1
                res = max(res, cur - num)
        return res