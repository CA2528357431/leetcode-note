class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        small = 0
        big = 0
        for i in range(1, n):
            if nums[i] < nums[small]:
                small = i
            if nums[i] > nums[big]:
                big = i
        ll = max(small, big) + 1
        rr = n - min(small, big)
        lr = (n - max(small, big)) + (min(small, big) + 1)
        return min(ll, rr, lr)