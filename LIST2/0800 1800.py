class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = -1
        cur = -1
        curs = 0
        for i in nums:
            if i <= cur:
                res = max(res, curs)
                cur = i
                curs = i
            else:
                cur = i
                curs += i

        res = max(curs, res)
        return res