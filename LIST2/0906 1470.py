class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        res=[0]*n
        for i in range(n//2):
            res[i*2]=nums[i]
            res[i*2+1]=nums[i+n//2]
        return res