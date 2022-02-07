class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        mid = 0
        for x in nums:
            if x<pivot:
                small.append(x)
            elif x>pivot:
                big.append(x)
            else:
                mid+=1
        return small+[pivot]*mid+big