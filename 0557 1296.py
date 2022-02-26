class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k > 0:
            return False
        nums.sort()
        cnt = Counter(nums)
        for x in nums:
            if cnt[x] == 0:
                continue
            for num in range(x, x + k):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True