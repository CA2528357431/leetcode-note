class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        li0 = []
        li1 = []
        for i in range(n):
            if i%2==0:
                li0.append(nums[i])
            else:
                li1.append(nums[i])
        li0.sort()
        li1.sort(reverse=True)
        for i in range(n):
            if i%2==0:
                nums[i]=li0[i//2]
            else:
                nums[i]=li1[i//2]
        return nums