class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        n = len(nums)
        for li in nums:
            s = s&set(li)
        li = list(s)
        li.sort()
        return li