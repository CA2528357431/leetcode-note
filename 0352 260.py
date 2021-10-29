class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for x in nums:
            res = res ^ x

        flag = res - (res & (res - 1))
        re1 = 0
        re2 = 0
        for x in nums:
            if flag & x == 0:
                re1 = re1 ^ x
            else:
                re2 = re2 ^ x

        return [re1, re2]