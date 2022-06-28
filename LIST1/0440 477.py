class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(30):
            c = 0
            for num in nums:
                get = (num>>i)&1
                c += get
            res += (n-c)*c
        return res

    # 按位数计算