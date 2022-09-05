class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        used = set()
        n = len(nums)
        for i in range(n-1):
            neo = nums[i]+nums[i+1]
            if neo in used:
                return True
            used.add(neo)
        return False