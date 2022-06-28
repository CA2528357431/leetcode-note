class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for x in nums:
            s ^= x
        return s

    # 两个一样的数字用 ^异或 必然为零
    # 相同的数字都抵消了