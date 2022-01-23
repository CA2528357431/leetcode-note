class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pos = 0
        neg = 0
        i = 0
        while pos < n and neg < n:
            while nums[pos] < 0:
                pos += 1
            res[i * 2] = nums[pos]

            while nums[neg] > 0:
                neg += 1
            res[i * 2 + 1] = nums[neg]

            pos += 1
            neg += 1
            i += 1
        return res