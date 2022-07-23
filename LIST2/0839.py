class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        dic = {}

        cur = 0
        for i in nums:
            if i == 0:
                cur += 1
            else:
                dic[cur] = dic.get(cur, 0) + 1
                cur = 0
        dic[cur] = dic.get(cur, 0) + 1
        res = 0
        for k in dic:
            v = dic[k]
            neo = (1 + k) * k // 2 * v
            res += neo
        return res
