class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1

        cur = 0
        for i in range(cnt):
            if nums[i] == 1:
                cur += 1
        res = cnt - cur

        for i in range(1, n):
            ii = (i + cnt - 1) % n
            if nums[i - 1] == nums[ii]:
                continue
            else:
                if nums[i - 1] == 0 and nums[ii] == 1:
                    cur += 1
                    res = min(res, cnt - cur)
                else:
                    cur -= 1
                    res = min(res, cnt - cur)

        return res