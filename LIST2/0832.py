class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def do(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        nums.sort(reverse=True)
        dic = {}
        used = set()
        res = -1
        for i in nums:
            neo = do(i)

            if neo in used:
                continue

            if neo in dic:
                re = i + dic[neo]
                res = max(res, re)
                used.add(neo)
            else:
                dic[neo] = i
        return res
