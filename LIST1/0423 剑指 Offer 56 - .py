class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        cur = 0
        for n in nums:
            cur = cur ^ n
        standard = cur&(-cur)
        a = 0
        b = 0
        for n in nums:
            if n&standard:
                a = a^n
            else:
                b = b^n
        return [a,b]