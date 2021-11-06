class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        length = [1] * n
        pre = [-1] * n

        big = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    pre[i] = j
            if length[i] > length[big]:
                big = i

        res = []
        while big >= 0:
            res.append(nums[big])
            big = pre[big]

        return res